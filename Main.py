from Tienda import Tienda
from Producto import Producto
from Usuario import Usuario
from Carrito import Carrito


def main():
    tienda = Tienda()
    producto1 = Producto("EA", "Producto 1", "Descripción del producto 1", 10, 100.0)
    producto2 = Producto("WE", "Producto 2", "Descripción del producto 2", 5, 50.0)
    producto3 = Producto("EA", "Producto 3", "Descripción del producto 3", 4, 30.0)
    usuario = Usuario(Carrito())
    tienda.agregar_producto_a_carrito(usuario, producto1, 11)
    tienda.agregar_producto_a_carrito(usuario, producto2, 1)
    tienda.agregar_producto_a_carrito(usuario, producto3, 3)
    tienda.eliminar_item_de_carrito(usuario, usuario.carrito.items[1])
    print(usuario.carrito.items)
    tienda.finalizar_compra(usuario)


if __name__ == "__main__":
    main()
