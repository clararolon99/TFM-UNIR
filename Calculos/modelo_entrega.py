"""Cálculo horario, eléctrico y económico para el TFM UNIR, entrega v0.2.

Ejecutar: python Calculos/modelo_entrega.py --salida Calculos
Requiere los dos ZIP de PVGIS contiguos y modelo_preliminar.py para leer
la transcripción anonimizada de las facturas y la función tarifaria.
El CSV corresponde al perfil de diseño, ajustado a la energía facturada.
"""

import argparse
import csv
import json
import math
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import mean
from zipfile import ZipFile

from modelo_preliminar import FACTURAS, cargo_energia

HERE = Path(__file__).resolve().parent
BILLS = FACTURAS[1:]
ENERGY = sum(f.kwh for f in BILLS)
BASE_CHARGE = sum(f.energia_gs for f in BILLS)
HOURS = sum(f.dias for f in BILLS) * 24
SHARES = (0.38, 0.33, 0.29)
AC_KW = 5.0
MODULE_KWP = 0.55
SLOPE = math.atan(0.30)
DAY = tuple(range(7, 19))
# Pesos relativos por hora local. La actividad representa usos agregados,
# sin implicar un inventario doméstico. La unidad kW se fija por las facturas.
ACTIVITY = (
    .36,.30,.27,.25,.26,.37,.78,1.03,.74,.64,.63,.75,
    .99,1.00,.77,.66,.70,.88,1.14,1.43,1.54,1.37,1.04,.60,
)
COOLING = (
    .75,.65,.55,.50,.45,.45,.40,.35,.35,.40,.50,.62,
    .72,.82,.90,.97,1.05,1.17,1.30,1.45,1.50,1.45,1.20,.92,
)
FIXED_BUDGET = {
    "Inversor trifásico de 5 kW, referencia de mercado": 12871000,
    "Medidor trifásico de control y enlace cableado": 1550000,
    "Cuadros, seccionamiento y protecciones CC/CA": 2450000,
    "Canalizaciones, cableado y puesta a tierra": 1600000,
    "Montaje, medios de acceso y mano de obra": 2650000,
    "Ingeniería y pruebas de recepción": 1300000,
}
MODULE_COST = 938000
MOUNT_COST = 310000
CONTINGENCY = 0.10
OM = 0.01
REPLACEMENT_COST = 8500000
REPLACEMENT_YEAR = 13
DISCOUNT = .08
DEGRADATION = .005
TERM = 20


def read_resource():
    """Conserva el mismo orden temporal de las tres orientaciones."""
    with ZipFile(HERE / "PVGIS_CDE_16_7_2021_2023.zip") as z:
        north = json.loads(z.read("norte.json"))["outputs"]["hourly"]
        south = json.loads(z.read("sur.json"))["outputs"]["hourly"]
    with ZipFile(HERE / "PVGIS_Ciudad_del_Este_2021_2023.zip") as z:
        horizontal = json.loads(z.read("pvgis-cde-horizontal-2021-2023.json"))["outputs"]["hourly"]
    series = defaultdict(dict)
    for n, s, h in zip(north, south, horizontal, strict=True):
        assert n["time"] == s["time"] == h["time"]
        utc = datetime.strptime(n["time"], "%Y%m%d:%H%M")
        local = utc - timedelta(hours=3)
        if local.year != utc.year:
            assert not any((n["P"], s["P"], n["G(i)"], s["G(i)"], h["G(i)"]))
            local = local.replace(year=utc.year)
        key = local.month, local.day, local.hour
        assert key not in series[utc.year]
        series[utc.year][key] = {
            "g_n": n["G(i)"] / 1000,
            "g_s": s["G(i)"] / 1000,
            "g_h": h["G(i)"] / 1000,
            "p_n": n["P"] / 1000,
            "p_s": s["P"] / 1000,
            "temp": n["T2m"],
        }
    assert list(series) == [2021, 2022, 2023]
    assert all(len(r) == 8760 for r in series.values())
    return series


def budget(modules):
    items = {"Módulos de 550 Wp": modules * MODULE_COST,
             "Estructura coplanar y fijaciones": modules * MOUNT_COST, **FIXED_BUDGET}
    direct = sum(items.values())
    items["Contingencia del 10 %"] = round(direct * CONTINGENCY)
    return items


def demand_weight(timestamp, temp, daytime):
    hour = timestamp.hour
    is_weekend = timestamp.weekday() >= 5
    if 6 <= hour < 9:
        activity_factor = .83 if is_weekend else 1
    elif 10 <= hour < 17:
        activity_factor = 1.16 if is_weekend else 1
    else:
        activity_factor = 1
    cooling = .12 * max(0, temp - 24) * COOLING[hour]
    load = .42 + ACTIVITY[hour] * activity_factor + cooling
    return load * (daytime if hour in DAY else 1)


def allocate(series, daytime=1):
    """Escala cada ciclo por separado para cerrar su balance exactamente."""
    results = []
    for f in BILLS:
        start = datetime.fromisoformat(f.inicio)
        hours = []
        for offset in range(f.dias * 24):
            t = start + timedelta(hours=offset)
            weather = series[t.month, t.day, t.hour]
            hours.append((t, weather, demand_weight(t, weather["temp"], daytime)))
        scale = f.kwh / sum(weight for _, _, weight in hours)
        results.append([(t, w, scale * weight) for t, w, weight in hours])
    return results


def alternative_pv(weather):
    """Comprobación independiente: NOCT, gamma y pérdidas explícitas, por kWp."""
    g = weather["g_n"]
    cell = weather["temp"] + (45 - 20) * g / .8
    derates = (.98, .985, .99, .995, .98, .975, .995)
    return g * max(0, 1 - .0035 * (cell - 25)) * math.prod(derates)


def run(cycles, modules, shares=SHARES, shade=0, orient="n", model="pvgis", keep_rows=False):
    assert math.isclose(sum(shares), 1) and min(shares) > 0
    phases = 3 * min(shares)
    reports = []
    rows = []
    by_hour = [[] for _ in range(24)]
    for f, hours in zip(BILLS, cycles, strict=True):
        agg = defaultdict(float)
        for t, w, d in hours:
            base = w["p_" + orient] if model == "pvgis" else alternative_pv(w)
            gross = modules * MODULE_KWP * base * (1 - shade)
            potential = min(AC_KW, gross)
            usable = min(potential, phases * d)
            bought = d - usable
            for key, val in dict(demand=d, gross=gross, potential=potential, usable=usable,
                                 grid=bought, clip=gross-potential, cut=potential-usable,
                                 daytime=d if t.hour in DAY else 0).items():
                agg[key] += val
            agg["peak"] = max(agg["peak"], d)
            by_hour[t.hour].append((d, potential, usable, bought))
            if keep_rows:
                rows.append((t.isoformat(timespec="minutes") + "-03:00", f.fin, w["temp"],
                             w["g_h"], w["g_" + orient], d, *(d * p for p in shares),
                             potential, usable, bought, potential - usable, 0.0))
        assert math.isclose(agg["demand"], f.kwh, abs_tol=1e-7)
        assert math.isclose(agg["grid"] + agg["usable"], f.kwh, abs_tol=1e-7)
        assert math.isclose(agg["clip"] + agg["cut"] + agg["usable"], agg["gross"], abs_tol=1e-7)
        agg["base_gs"] = f.energia_gs
        agg["post_gs"] = cargo_energia(agg["grid"])
        agg["saving"] = agg["base_gs"] - agg["post_gs"]
        reports.append(dict(agg))
    sums = {k: sum(r[k] for r in reports) for k in reports[0] if k != "peak"}
    assert math.isclose(sums["demand"], ENERGY, abs_tol=1e-7)
    sums["peak"] = max(r["peak"] for r in reports)
    return {"totals": sums, "cycles": reports, "rows": rows,
            "typical": [[mean(v) for v in zip(*hours, strict=True)] for hours in by_hour]}


def average(results):
    return {key: mean(result["totals"][key] for result in results)
            for key in results[0]["totals"]}


def npv(flows, rate):
    return sum(cash / (1 + rate)**t for t, cash in enumerate(flows))


def irr(flows):
    low, high = -.5, 1
    if npv(flows, low) <= 0 or npv(flows, high) >= 0:
        return None
    for _ in range(60):
        mid = (low + high) / 2
        if npv(flows, mid) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def finance(runs, modules, rate=DISCOUNT, tariff=1, capex_factor=1, replacement=REPLACEMENT_COST):
    capex = sum(budget(modules).values()) * capex_factor
    savings = [mean(
        sum(bill.energia_gs - cargo_energia(bill.kwh - row["usable"] * (1 - DEGRADATION)**(y - 1))
            for row, bill in zip(run["cycles"], BILLS, strict=True))
        for run in runs) * tariff for y in range(1, TERM + 1)]
    flows = [-capex] + [a - OM * capex - (replacement if i == REPLACEMENT_YEAR else 0)
                        for i, a in enumerate(savings, 1)]
    d_flows = [value/(1+rate)**t for t, value in enumerate(flows)]
    cum = [sum(flows[:t+1]) for t in range(TERM+1)]
    cum_d = [sum(d_flows[:t+1]) for t in range(TERM+1)]
    payback = next((t for t in range(1, TERM+1) if min(cum[t:]) >= 0), None)
    payback_d = next((t for t in range(1, TERM+1) if min(cum_d[t:]) >= 0), None)
    gross_pv = npv([0] + savings, rate)
    replacement_pv = replacement / (1+rate)**REPLACEMENT_YEAR
    annuity = sum(1/(1+rate)**t for t in range(1, TERM+1))
    pv_used = sum(average(runs)["usable"] * (1 - DEGRADATION)**(t-1) / (1+rate)**t
                  for t in range(1, TERM+1))
    return {"capex": capex, "npv": sum(d_flows), "irr": irr(flows), "payback": payback,
            "discounted_payback": payback_d, "gross_pv": gross_pv,
            "lcoe_use": (capex * (1 + OM * annuity) + replacement_pv) / pv_used,
            "threshold": (gross_pv - replacement_pv) / (1 + OM * annuity),
            "tariff_threshold": (capex * (1 + OM * annuity) + replacement_pv) / gross_pv,
            "cum": cum, "cum_discounted": cum_d, "savings": savings, "flows": flows}


def check_electrical():
    module_area = 2.274 * 1.134
    voc_cold = 10 * 49.62 * (1 + .0028 * (25 - (-5)))
    vmp_hot = 10 * 40.90 * (1 - .0040 * (85 - 25))
    isc_design = 1.25 * 14.03
    dc_drop = 2 * .0225 * 25 * 13.45 / 6
    ac_current = 5000 / (math.sqrt(3) * 380)
    ac_drop = math.sqrt(3) * .0225 * 20 * 8.3 / 4
    return dict(area=module_area * 10, roof_degrees=math.degrees(SLOPE),
                v_oc_cold=voc_cold, v_mp_hot=vmp_hot, isc_design=isc_design,
                drop_dc_v=dc_drop, drop_dc_pct=100*dc_drop/vmp_hot,
                ac_current=ac_current, drop_ac_v=ac_drop, drop_ac_pct=100*ac_drop/380,
                layout_width=3*1.134+.04,
                layout_length=(3*2.274 + 1.134)*math.cos(SLOPE)+.60+.04)


def main(out):
    assert all(cargo_energia(f.kwh) == f.energia_gs for f in FACTURAS)
    series = read_resource()
    allocations = {factor: {year: allocate(weather, factor) for year, weather in series.items()}
                   for factor in (.75, 1, 1.25)}
    core = [run(cycles, 10, keep_rows=(year == 2022)) for year, cycles in allocations[1].items()]
    layouts = []
    for n in (6, 8, 10, 12):
        result = [run(cycles, n) for cycles in allocations[1].values()]
        layouts.append({"n":n, **average(result), "economy":finance(result, n)})
    effects = []
    cases = [
        ("Carga vespertina", .75, SHARES, 0, "n", "pvgis"),
        ("Caso central", 1, SHARES, 0, "n", "pvgis"),
        ("Carga diurna", 1.25, SHARES, 0, "n", "pvgis"),
        ("Fases casi equilibradas", 1, (.34,.33,.33), 0, "n", "pvgis"),
        ("Fase débil con 22 %", 1, (.43,.35,.22), 0, "n", "pvgis"),
        ("Control por saldo total ideal", 1, (1/3,1/3,1/3), 0, "n", "pvgis"),
        ("Pérdida adicional del 10 %", 1, SHARES, .10, "n", "pvgis"),
        ("Plano hacia el sur", 1, SHARES, 0, "s", "pvgis"),
        ("Comprobación NOCT", 1, SHARES, 0, "n", "noct"),
    ]
    for label, factor, phases, shade, orient, model in cases:
        result = [run(cycles, 10, phases, shade, orient, model)
                  for cycles in allocations[factor].values()]
        effects.append({"name": label, **average(result)})
    economical = []
    for name, kw in (
        ("Base", {}), ("Inversión −20 %", {"capex_factor":.8}),
        ("Tarifa +25 %", {"tariff":1.25}), ("Tarifa +50 %", {"tariff":1.5}),
        ("Descuento 5 %", {"rate":.05}), ("Descuento 11 %", {"rate":.11}),
        ("Sin recambio en el horizonte", {"replacement":0}),
        ("Inversión −20 % y tarifa +50 %", {"capex_factor":.8, "tariff":1.5}),
    ):
        economical.append({"name":name, **finance(core, 10, **kw)})
    monthly = []
    for month in range(1, 13):
        values = [r for w in series.values() for (m,_,_),r in w.items() if m == month]
        monthly.append({k:sum(r[k] for r in values)/len(series) for k in ("g_n","g_s","g_h","p_n","p_s")})
    annual = [{"year":year, **{k:sum(r[k] for r in w.values()) for k in ("g_n","g_s","g_h","p_n","p_s")},
               "t_min":min(r["temp"] for r in w.values()), "t_max":max(r["temp"] for r in w.values()),
               "t_mean":mean(r["temp"] for r in w.values()), **result["totals"]}
              for (year,w),result in zip(series.items(),core,strict=True)]
    csv_rows = core[1]["rows"]
    assert len(csv_rows) == HOURS == 8736
    out.mkdir(parents=True, exist_ok=True)
    with (out / "Perfil_horario_diseno_v0.2.csv").open("w",encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f,delimiter=";")
        writer.writerow(("inicio_hora_UTC-03","fin_ciclo_exclusivo","temp_ref_C","GHI_kWh_m2",
                         "POA_kWh_m2","demanda_kWh","L1_kWh","L2_kWh","L3_kWh","FV_disponible_kWh",
                         "FV_consumida_kWh","compra_kWh","recorte_control_kWh","inyeccion_objetivo_kWh"))
        writer.writerows([t,end,*(f"{v:.8f}" for v in vals)] for t,end,*vals in csv_rows)
    result = {
        "bills":[{**vars(f),"days":f.dias} for f in FACTURAS], "hours":HOURS,
        "base_gs":BASE_CHARGE,"demand_kwh":ENERGY, "bill_total":sum(f.total_gs for f in BILLS),
        "central":average(core),"annual":annual, "monthly_resource":monthly,
        "cycles":[{k:mean(r["cycles"][i][k] for r in core) for k in core[0]["cycles"][i]}
                  for i in range(len(BILLS))],
        "typical":[[mean(r["typical"][h][i] for r in core) for i in range(4)] for h in range(24)],
        "layouts":layouts,"scenarios":effects,"economic_sensitivities":economical,
        "budget":budget(10),"electrical":check_electrical(),
    }
    (out / "Resultados_v0.2.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("central","electrical")},indent=2))
    for row in layouts:
        e=row["economy"]
        print(row["n"], round(row["usable"]), round(row["saving"]), round(e["npv"]),
              round(e["threshold"]), e["irr"], e["payback"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida",type=Path,default=HERE)
    main(parser.parse_args().salida)
