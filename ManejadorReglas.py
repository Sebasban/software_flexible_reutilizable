from ReglaPrecio import (
    ReglaPrecio,
    ReglaPrecioNormal,
    ReglaPrecioPorPeso,
    ReglaPrecioEspecial,
)


class ManejadorReglas:
    @staticmethod
    def obtener_regla(sku) -> ReglaPrecio:
        reglas = {}
        reglas[ReglaPrecioNormal()] = ReglaPrecioNormal().es_aplicable(sku)
        reglas[ReglaPrecioEspecial()] = ReglaPrecioEspecial().es_aplicable(sku)
        reglas[ReglaPrecioPorPeso()] = ReglaPrecioPorPeso().es_aplicable(sku)
        return reglas
