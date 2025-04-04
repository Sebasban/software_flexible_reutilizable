class Producto:
    def __init__(self, sku, nombre, descripcion, unidades_disponibles, precio_unitario):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.unidades_disponibles = unidades_disponibles
        self.precio_unitario = precio_unitario

    def tiene_unidades(self, cantidad) -> bool:
        if self.unidades_disponibles >= cantidad:
            self.descontar_unidades(cantidad)
            return True
        return False

    def descontar_unidades(self, cantidad):
        self.unidades_disponibles -= cantidad
