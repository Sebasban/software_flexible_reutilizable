from abc import ABC, abstractmethod


class ReglaPrecio(ABC):
    @abstractmethod
    def es_aplicable(self, sku) -> bool:
        pass

    @abstractmethod
    def calcular_total(self, cantidad, precio):
        pass


class ReglaPrecioNormal(ReglaPrecio):
    def es_aplicable(self, sku) -> bool:
        return sku == "EA"

    def calcular_total(self, cantidad, precio):
        return precio * cantidad


class ReglaPrecioPorPeso(ReglaPrecio):
    def es_aplicable(self, sku):
        return sku == "WE"

    def calcular_total(self, cantidad, precio):
        return cantidad * precio * 1000


class ReglaPrecioEspecial(ReglaPrecio):
    def es_aplicable(self, sku):
        return sku == "SP"

    def calcular_total(self, cantidad, precio):
        if cantidad > 2 and cantidad <= 3:
            return cantidad * precio * 0.8
        if cantidad > 3 and cantidad <= 6:
            return cantidad * precio * 0.6
        if cantidad > 6:
            return cantidad * precio * 0.5
        else:
            return cantidad * precio
