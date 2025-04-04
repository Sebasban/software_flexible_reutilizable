from ManejadorReglas import ManejadorReglas


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_total(self) -> float:
        regla = ManejadorReglas.obtener_regla(self.producto.sku)
        reglas_aplicables = [clave for clave, valor in regla.items() if valor]
        ret = reglas_aplicables[0].calcular_total(
            self.cantidad, self.producto.precio_unitario
        )
        print(f"Precio: {ret}", "$")
        return ret
