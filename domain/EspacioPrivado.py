import random

from domain.Espacio import Espacio


class EspacioPrivado(Espacio):

    def __init__(self, lugar, valor):
        super().__init__(self, lugar, valor)

    def __str__(self):
        return super().__str__() + " [Privado] Valor: " + str(self.__valor)
