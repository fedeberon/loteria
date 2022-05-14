import random

from domain.Espacio import Espacio


class EspacioPrivado(Espacio):
    __valor_privado = random.randint(0, 100)

    def __init__(self, ubicacion):
        super().__init__(ubicacion)  # Llamada al constructor de la clase padre

    def get_valor_privado(self):
        return self.__valor_privado

    def __str__(self):
        return super().__str__() + " [Privado] valor: " + str(self.__valor_privado)
