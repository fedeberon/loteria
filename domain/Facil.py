import names

from domain.EspacioPrivado import EspacioPrivado
from domain.Juego import Juego


class Facil(Juego):

    def __init__(self):
        self.__nombre = names.get_full_name()

    def ingresarEspacios(self, espacio_publico):
        super().__espacioPrivado = [EspacioPrivado(1), EspacioPrivado(2)]
        super().__espacioPublico = espacio_publico

    @property
    def cantidadDeEspacios(self):
        return len(self.__espacio_privado)

    def getEspacios(self):
        return self.__espacio_privado

    def __str__(self):
        return self._nombre + " - Nivel Facil"
