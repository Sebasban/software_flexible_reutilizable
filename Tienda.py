class Tienda:
    def __init__(self):
        self.total_ventas = 0

    def agregar_producto_a_carrito(self, usuario, producto, cantidad):
        if producto.tiene_unidades(cantidad):
            usuario.agregar_item_a_carrito(producto, cantidad)
        else:
            print("No hay suficientes unidades disponibles.")

    def eliminar_item_de_carrito(self, usuario, item):
        usuario.eliminar_producto_de_carrito(item)

    def finalizar_compra(self, usuario):
        precio_final = usuario.carrito.calcular_total()
        print(f"finalizar compra el total completo: {precio_final}")
