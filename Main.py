from Tienda import Tienda
from Producto import Producto
from Usuario import Usuario
from Carrito import Carrito


def main():
    tienda = Tienda()
    producto1 = Producto("EA", "Producto 1", "Descripción del producto 1", 10, 100.0)
    producto2 = Producto("WE", "Producto 2", "Descripción del producto 2", 5, 50.0)
    producto3 = Producto("SP", "Producto 3", "Descripción del producto 3", 0, 25.0)
    usuario = Usuario(Carrito())
    tienda.agregar_producto_a_carrito(usuario, producto1, 2)
    tienda.agregar_producto_a_carrito(usuario, producto2, 1)
    print(usuario.carrito.items)
    tienda.finalizar_compra(usuario)


if __name__ == "__main__":
    main()
