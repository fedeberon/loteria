from abc import ABC


# Clase abstracta desde donde se definen los comportamientos comunes a todos los Espacios
class Espacio(ABC):
    lugar: int
    valor: int

    # Constructor de la clase Espacio.
    def __init__(self, lugar, valor):
        self.lugar = lugar
        self.valor = valor

    # Método para definirle valores a la propiedad valor.
    # Esto es ENCAPSULAMIENTO, ya que no se puede acceder directamente a la propiedad valor.
    def setValor(self, valor):
        self.valor = valor

    # Método para definirle valores a la propiedad lugar.
    # Esto es ENCAPSULAMIENTO, ya que no se puede acceder directamente a la propiedad valor.
    def setLugar(self, lugar):
        self.lugar = lugar
