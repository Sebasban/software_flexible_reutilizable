class Usuario:
    def __init__(self, carrito):
        self.carrito = carrito

    def agregar_item_a_carrito(self, producto, cantidad):
        self.carrito.agregar_item(producto, cantidad)

    def eliminar_producto_de_carrito(self, item):
        self.carrito.borrar_item(item)
