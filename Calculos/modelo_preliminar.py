"""Balance horario reproducible para el borrador v0.1 del TFM de UNIR.

Ejecutar: python modelo_preliminar.py
Lee el ZIP de PVGIS contiguo e imprime resultados en JSON. Los datos
energéticos se cotejaron con los 13 PDF de facturación de ANDE.
"""

import json
import math
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import mean
from zipfile import ZipFile


@dataclass(frozen=True)
class Factura:
    inicio: str
    fin: str
    kwh: int
    energia_gs: int
    total_gs: int

    @property
    def dias(self):
        return (date.fromisoformat(self.fin) - date.fromisoformat(self.inicio)).days


FACTURAS = (
    Factura("2025-06-27", "2025-07-26", 795, 334115, 403000),
    Factura("2025-07-26", "2025-08-28", 780, 327811, 388000),
    Factura("2025-08-28", "2025-09-27", 752, 316043, 375000),
    Factura("2025-09-27", "2025-10-28", 951, 399677, 483000),
    Factura("2025-10-28", "2025-11-27", 968, 406821, 493000),
    Factura("2025-11-27", "2025-12-23", 1186, 516515, 616000),
    Factura("2025-12-23", "2026-01-24", 1595, 694638, 791000),
    Factura("2026-01-24", "2026-02-24", 1698, 739496, 1005000),
    Factura("2026-02-24", "2026-03-26", 1541, 671121, 766000),
    Factura("2026-03-26", "2026-04-25", 1246, 542645, 624000),
    Factura("2026-04-25", "2026-05-26", 732, 307638, 365000),
    Factura("2026-05-26", "2026-06-25", 687, 288725, 386000),
    Factura("2026-06-25", "2026-07-25", 822, 345462, 459000),
)

# Pliego de Tarifas ANDE N.º 21, sección 5.1.1.2, categoría 142.
# Los precios en centésimos de guaraní permiten replicar el redondeo.
FAJAS = (
    (50, 31155), (150, 34989), (300, 36545),
    (500, 40382), (1000, 42027), (math.inf, 43551),
)


def cargo_energia(kwh, minimo=120):
    energia_facturable = max(minimo, math.floor(kwh + 0.5))
    precio = next(precio for limite, precio in FAJAS if energia_facturable <= limite)
    return (energia_facturable * precio + 50) // 100


@dataclass(frozen=True)
class Hora:
    local: datetime
    potencial: float
    horizontal: float
    inclinada: float


def series_locales(archivo):
    with ZipFile(archivo) as datos:
        fv = json.loads(datos.read("pvgis-cde-norte-2021-2023.json"))
        horizontal = json.loads(datos.read("pvgis-cde-horizontal-2021-2023.json"))
    horas = defaultdict(list)
    for mod, plano in zip(fv["outputs"]["hourly"], horizontal["outputs"]["hourly"], strict=True):
        if mod["time"] != plano["time"]:
            raise ValueError("Las dos series PVGIS tienen marcas horarias distintas.")
        utc = datetime.strptime(mod["time"], "%Y%m%d:%H%M")
        local = utc - timedelta(hours=3)
        if local.year != utc.year:
            # Trasladar al cierre del mismo año sus tres horas iniciales UTC.
            # Se verifica que estas horas nocturnas tienen radiación y potencia nulas.
            if mod["P"] or mod["G(i)"] or plano["G(i)"]:
                raise ValueError("El ajuste de borde trasladaría producción solar.")
            local = local.replace(year=utc.year)
        horas[local.year].append(Hora(local, mod["P"] / 1000, plano["G(i)"] / 1000, mod["G(i)"] / 1000))
    if set(horas) != {2021, 2022, 2023}:
        raise ValueError("Se esperaban tres años de meteorología de 2021 a 2023.")
    for anio, datos in horas.items():
        datos.sort(key=lambda hora: hora.local)
        inicio = datetime(anio, 1, 1, 0, 30)
        if len(datos) != 8760 or any(
            hora.local != inicio + timedelta(hours=i) for i, hora in enumerate(datos)
        ):
            raise ValueError(f"La serie local de {anio} tiene horas faltantes o duplicadas.")
    return horas


def dias_por_ciclo(facturas):
    """Asocia el mes y día con el ciclo de lectura y su consumo medio diario."""
    dias = {}
    for ciclo, factura in enumerate(facturas):
        inicio = date.fromisoformat(factura.inicio)
        for i in range(factura.dias):
            dia = inicio + timedelta(days=i)
            clave = (dia.month, dia.day)
            if clave in dias:
                raise ValueError("Los ciclos de facturación se solapan.")
            dias[clave] = (ciclo, factura.kwh / factura.dias)
    return dias


def evaluar(horas, facturas, potencia, fraccion_diurna, sombra):
    carga_diaria = dias_por_ciclo(facturas)
    kwh_demanda = sum(f.kwh for f in facturas)
    cargo_base = sum(cargo_energia(f.kwh) for f in facturas)
    anuales = []
    for anio, registros in sorted(horas.items()):
        potencial = autoconsumo = demanda = 0.0
        compras_por_ciclo = defaultdict(float)
        for hora in registros:
            fecha = (hora.local.month, hora.local.day)
            if fecha not in carga_diaria:
                continue
            ciclo, consumo_diario = carga_diaria[fecha]
            fraccion = fraccion_diurna if 7 <= hora.local.hour < 19 else 1 - fraccion_diurna
            carga = consumo_diario * fraccion / 12
            produccion = hora.potencial * potencia * (1 - sombra)
            uso = min(carga, produccion)
            potencial += produccion
            demanda += carga
            autoconsumo += uso
            compras_por_ciclo[ciclo] += carga - uso
        compra = sum(compras_por_ciclo.values())
        if not math.isclose(demanda, kwh_demanda) or not math.isclose(compra + autoconsumo, demanda):
            raise ValueError("El balance anual no conserva la energía de demanda.")
        anuales.append({
            "anio": anio,
            "potencial_kwh": potencial,
            "autoconsumo_kwh": autoconsumo,
            "compra_kwh": compra,
            "recorte_kwh": potencial - autoconsumo,
            "ahorro_gs": cargo_base - sum(cargo_energia(kwh) for kwh in compras_por_ciclo.values()),
            "importacion_minima_por_ciclo_kwh": min(compras_por_ciclo.values()),
        })
    promedios = {
        clave: mean(fila[clave] for fila in anuales)
        for clave in ("potencial_kwh", "autoconsumo_kwh", "compra_kwh", "recorte_kwh", "ahorro_gs")
    }
    ahorro = promedios["ahorro_gs"]
    descuento = [1 / 1.08**t for t in range(1, 21)]
    ahorros_actualizados = sum(ahorro * 0.995**i * factor for i, factor in enumerate(descuento))
    return {
        "potencia_kwp": potencia,
        "fraccion_diurna": fraccion_diurna,
        "sombra": sombra,
        **promedios,
        "cobertura_pct": 100 * promedios["autoconsumo_kwh"] / kwh_demanda,
        "uso_produccion_pct": 100 * promedios["autoconsumo_kwh"] / promedios["potencial_kwh"],
        "ahorro_cargo_pct": 100 * ahorro / cargo_base,
        "inversion_umbral_gs": ahorros_actualizados / (1 + 0.01 * sum(descuento)),
        "anuales": anuales,
    }


def main():
    insumos = Path(__file__).with_name("PVGIS_Ciudad_del_Este_2021_2023.zip")
    horas = series_locales(insumos)
    facturas = FACTURAS[1:]
    if any(cargo_energia(f.kwh) != f.energia_gs for f in FACTURAS):
        raise ValueError("El Pliego N.º 21 no reproduce los cargos de energía transcritos.")
    recurso = []
    for anio, registros in sorted(horas.items()):
        recurso.append({
            "anio": anio,
            "horizontal_kwh_m2": sum(hora.horizontal for hora in registros),
            "inclinada_kwh_m2": sum(hora.inclinada for hora in registros),
            "rendimiento_kwh_kwp": sum(hora.potencial for hora in registros),
        })
    meses = []
    for mes in range(1, 13):
        registros = [hora for serie in horas.values() for hora in serie if hora.local.month == mes]
        meses.append({
            "mes": mes,
            "horizontal_kwh_m2": sum(hora.horizontal for hora in registros) / len(horas),
            "inclinada_kwh_m2": sum(hora.inclinada for hora in registros) / len(horas),
            "rendimiento_kwh_kwp": sum(hora.potencial for hora in registros) / len(horas),
        })
    escenarios = [
        evaluar(horas, facturas, potencia, fraccion, sombra)
        for potencia in (3.3, 5.5, 7.7)
        for fraccion in (0.3, 0.5, 0.7)
        for sombra in (0.0, 0.1, 0.2)
    ]
    print(json.dumps({
        "facturas": [{**vars(f), "dias": f.dias} for f in FACTURAS],
        "dias_referencia": sum(f.dias for f in facturas),
        "demanda_referencia_kwh": sum(f.kwh for f in facturas),
        "cargo_base_gs": sum(f.energia_gs for f in facturas),
        "facturacion_total_gs": sum(f.total_gs for f in facturas),
        "recurso": recurso,
        "recurso_mensual_medio": meses,
        "escenarios": escenarios,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
