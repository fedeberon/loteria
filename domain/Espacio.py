from abc import ABC


class Espacio(ABC):

    __lugar: int
    __valor: int

    def __init__(self, lugar, valor):
        self.__lugar = lugar
        self.__valor = valor

    def setValor(self, valor):
            super().__valor = valor

    def setLugar(self, lugar):
        super().__lugar = lugar
