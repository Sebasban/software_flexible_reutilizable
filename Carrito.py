from Item import Item


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto, cantidad):
        self.item = Item(producto, cantidad)
        self.items.append(self.item)

    def calcular_total(self) -> float:
        total = 0
        for item in self.items:  # Itera sobre todos los items en el carrito
            total += item.calcular_total()
        return total

    def mostrar_item(self):
        return self.items

    def borrar_item(self, item):
        self.items.remove(item)
