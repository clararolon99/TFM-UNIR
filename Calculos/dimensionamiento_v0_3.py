"""Dimensionamiento v0.3 del TFM y contraste horario.

Ejecutar con Python 3.10+: python Calculos/dimensionamiento_v0_3.py
Lee las facturas anonimizadas y las series PVGIS conservadas en Calculos.
"""

import json
import math
from calendar import monthrange
from pathlib import Path
from statistics import mean
from zipfile import ZipFile

import modelo_entrega as prev

HERE = Path(__file__).resolve().parent
PR_DESIGN = .75
G_STC = 1.0
TILT = math.atan(.30)
LAT = -25.51
SLOPE = .30
NOMINAL_KW = 5.0
RATIO_CC_CA = 1.10
MODULE_KWP = .550
VOC = 50.10
VMP = 42.13
ISC = 13.90
IMP = 13.06
MODULE_LONG = 2.279
MODULE_WIDE = 1.134
COLD = -5
HOT = 85
VOC_COEFF = -.0025
VMP_COEFF = -.0039  # aproximación: gamma Pmax - alfa Isc
TOL = .03
CC_LENGTH = 25
CA_LENGTH = 20
CC_SECTION = 6
CA_SECTION = 4
RHO_CU = .0225
MAX_AC_CURRENT = 8.5
V_LINE = 380
DC_DROP_LIMIT = .015
AC_DROP_LIMIT = .01
BASE_EQUIPMENT = (
    ("Inversor Huawei SUN2000-5KTL-M1", "ud.", 1, 12871000, "Nissei/Electropar. SKU 129564"),
    ("Medidor DTSU666-H compatible y enlace", "juego", 1, 1550000, "Provisión"),
    ("Cable solar Cu 6 mm²", "m", 50, 11500, "Provisión"),
    ("Cable de potencia 5G4 mm² Cu", "m", 20, 57000, "Provisión"),
    ("Equipotencial de Cu 6 mm² y terminales", "m", 30, 14000, "Provisión"),
    ("Enlace de comunicación RS-485", "m", 30, 6000, "Provisión"),
    ("DPS FV tipo 2", "ud.", 2, 440000, "Provisión"),
    ("DPS CA tipo 2 para TT", "ud.", 1, 550000, "Provisión"),
    ("Seccionador CC bipolar", "ud.", 1, 380000, "Provisión"),
    ("Interruptor automático CA 16 A", "ud.", 1, 245000, "Provisión"),
    ("Diferencial CA tetrapolar tipo A, 100 mA", "ud.", 1, 520000, "Provisión"),
    ("Envolventes CC y CA", "ud.", 2, 310000, "Provisión"),
    ("Canalización y fijaciones de recorrido", "m", 45, 12000, "Provisión"),
    ("Conectores, borne, rótulos y consumibles", "juego", 1, 350000, "Provisión"),
    ("Revisión y adecuación de tierra", "juego", 1, 450000, "Provisión"),
    ("Transporte de equipos", "servicio", 1, 350000, "Provisión"),
    ("Montaje, acceso y mano de obra", "servicio", 1, 2650000, "Provisión"),
    ("Ingeniería y pruebas de recepción", "servicio", 1, 1300000, "Provisión"),
)


def budget(n):
    rows = [
        ("Módulo YH SUNPRO YHP550W", "ud.", n, 954000, "MP Energía Propia"),
        ("Perfiles Romagnole RS-327, 4,80 m", "ud.", 8 if n==10 else max(4,math.ceil(n*.8)), 165000, "Provisión"),
        ("Anclajes para teja, familia RS-223", "ud.", 30 if n==10 else 3*n, 45000, "Provisión"),
        ("Grapas finales para marco de 30 mm", "ud.", 16 if n==10 else 2*n, 12500, "Provisión"),
        ("Grapas intermedias", "ud.", 12 if n==10 else n, 12500, "Provisión"),
        ("Accesorios de estructura y equipotencial", "juego", 1, 130000, "Provisión basada en CYPE"),
        *BASE_EQUIPMENT,
    ]
    subtotal = sum(q * unit for _, _, q, unit, _ in rows)
    rows.append(("Contingencia de obra", "partida", 1, round(subtotal*.10), "10 % del coste directo"))
    return {"rows": rows, "direct": subtotal, "total": sum(q*unit for _,_,q,unit,_ in rows)}


def variant_resource():
    with ZipFile(HERE/"PVGIS_CDE_21_3_2021_2023.zip") as data:
        rows = json.loads(data.read("norte_21_3.json"))["outputs"]["hourly"]
    assert len(rows) == 3*8760
    return (sum(r["G(i)"] for r in rows)/3000, sum(r["P"] for r in rows)/3000)


def main():
    meteo = prev.read_resource()
    cycles = {year: prev.allocate(weather) for year, weather in meteo.items()}
    cases = {n: [prev.run(series,n) for series in cycles.values()] for n in (6,8,10,12)}
    core = prev.average(cases[10])
    demand = sum(f.kwh for f in prev.BILLS)
    days = sum(f.dias for f in prev.BILLS)
    share = core["daytime"]/demand
    E_daily = demand / days
    E_target = E_daily * share
    klist = ("g_h","g_n","g_s","p_n","p_s")
    mean_resources = {k: mean(sum(r[k] for r in year.values()) for year in meteo.values()) for k in klist}
    hsp = mean_resources["g_n"] / (365*G_STC)
    required_kwp = E_target/(hsp*PR_DESIGN)
    n = math.ceil(required_kwp/MODULE_KWP)
    p = n*MODULE_KWP
    assert n == 10 and math.isclose(p,prev.MODULE_KWP*10)
    yearly = p*hsp*365*PR_DESIGN
    grid_check = p*mean_resources["p_n"]
    month_h = [mean(sum(r["g_n"] for key,r in year.items() if key[0]==m)
                    for year in meteo.values()) for m in range(1,13)]
    monthly = [{"month":m, "H":value, "hsp":value/monthrange(2022,m)[1]/G_STC,
                "yield":value*p*PR_DESIGN/G_STC}
               for m,value in enumerate(month_h,1)]
    alt_h,alt_y = variant_resource()
    cold = n*VOC*(1+TOL)*(1+VOC_COEFF*(COLD-25))
    hot = n*VMP*(1+VMP_COEFF*(HOT-25))
    isc = ISC*(1+TOL)*1.25
    cc_max_volts = DC_DROP_LIMIT*hot
    ca_max_volts = AC_DROP_LIMIT*V_LINE
    cc_min_s = 2*RHO_CU*CC_LENGTH*isc/cc_max_volts
    ca_min_s = math.sqrt(3)*RHO_CU*CA_LENGTH*MAX_AC_CURRENT/ca_max_volts
    cc_drop = 2*RHO_CU*CC_LENGTH*isc/CC_SECTION
    ca_drop = math.sqrt(3)*RHO_CU*CA_LENGTH*MAX_AC_CURRENT/CA_SECTION
    assert cc_drop <= cc_max_volts and ca_drop <= ca_max_volts
    assert cold < 1100 and 200 < hot < 980 and isc < 19.5 and IMP < 13.5
    setback = (9.18 - ((3*MODULE_LONG+MODULE_WIDE)*math.cos(TILT) + .64))/2
    assert setback > .40
    roof = {"width":3*MODULE_WIDE+.04, "length":9.18-2*setback, "end_margin":setback,
            "panel_area":n*MODULE_LONG*MODULE_WIDE,
            "projection":n*MODULE_LONG*MODULE_WIDE*math.cos(TILT),
            "horizontal_shadow_example": MODULE_LONG*math.sin(TILT)/math.tan(math.radians(90-abs(LAT-23.44))),
            "weight_kg": n*27, "service_load_kPa":(n*27+60)*9.81/1000/(n*MODULE_LONG*MODULE_WIDE*math.cos(TILT))}
    economics = []
    for count,runs in cases.items():
        costs=budget(count)
        factor=costs["total"]/sum(prev.budget(count).values())
        e=prev.finance(runs,count,capex_factor=factor)
        economics.append({"count":count,"kwp":count*MODULE_KWP,**prev.average(runs), "economics":e})
    capex_factor = budget(n)["total"]/sum(prev.budget(n).values())
    sensitivities=[]
    for title,modifiers in (
        ("Base",{}),("Inversión −20 %",{"capex_factor":.80*capex_factor}),
        ("Tarifa +25 %",{"tariff":1.25}),("Tarifa +50 %",{"tariff":1.5}),
        ("Descuento 5 %",{"rate":.05}),("Descuento 11 %",{"rate":.11}),
        ("Sin recambio",{"replacement":0}),
        ("Inversión −20 % y tarifa +50 %",{"capex_factor":.80*capex_factor,"tariff":1.5}),
    ):
        args={"capex_factor":capex_factor,**modifiers}
        sensitivities.append({"name":title,**prev.finance(cases[10],10,**args)})
    d={
        "demand":demand,"days":days,"daily":E_daily,"share":share,"target":E_target,"central":core,
        "H":mean_resources,"hsp":hsp,"required_kwp":required_kwp,"required_full_kwp":E_daily/(hsp*PR_DESIGN),
        "required_winter_kwp":E_target/(min(m["hsp"] for m in monthly)*PR_DESIGN),
        "pr":PR_DESIGN,"n":n,"kwp":p,"yield_daily":yearly/365,"annual_hand":yearly,"annual_pvgis":grid_check,
        "annual_21p3_h":alt_h,"annual_21p3_specific":alt_y,"annual_21p3_kwh":alt_y*p,
        "annual_21p3_delta_pct":100*(alt_y/mean_resources["p_n"]-1),"months":monthly,
        "ca_needed":p/RATIO_CC_CA,"ca_kw":NOMINAL_KW,"ratio":p/NOMINAL_KW,
        "cold_voc":cold,"hot_vmp":hot,"stc_vmp":n*VMP,"stc_voc":n*VOC,"isc_design":isc,
        "ca_nominal_a":1000*NOMINAL_KW/(math.sqrt(3)*V_LINE),
        "cc_min_s":cc_min_s,"ca_min_s":ca_min_s,"cc_drop":cc_drop,"ca_drop":ca_drop,
        "cc_drop_pct":100*cc_drop/hot,"ca_drop_pct":100*ca_drop/V_LINE,
        "cc_drop_operating":2*RHO_CU*CC_LENGTH*IMP/CC_SECTION,
        "roof":roof,"budget":budget(n),"layouts":economics,"sensitivities":sensitivities,
    }
    dest=HERE/"Resultados_v0.3.json"
    dest.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"{dest.name}: {days} días, {demand} kWh, {required_kwp:.4f} kWp requeridos, {n} módulos.")
    print(f"Producción por fórmula {yearly:.2f} kWh/año. PVGIS {grid_check:.2f} kWh/año.")
    print(f"CAPEX {d['budget']['total']:,} Gs. VAN {economics[2]['economics']['npv']:,.0f} Gs.")
    print(f"Secciones mínimas por caída: CC {cc_min_s:.3f} mm². CA {ca_min_s:.3f} mm².")


if __name__ == "__main__":
    main()
