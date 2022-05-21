import names

from domain.EspacioPrivado import EspacioPrivado
from domain.Juego import Juego


class Dificil(Juego):
    __espacio_privado = [EspacioPrivado(1), EspacioPrivado(2), EspacioPrivado(3), EspacioPrivado(4), EspacioPrivado(5)]
    __espacio_publico = None

    def cantidadDeEspacios(self):
        pass

    def ingresarEspacios(self, espacios):
        pass

    def __init__(self):
        self._nombre = names.get_full_name()

    def __str__(self):
        return self._nombre + " - Nivel Dificil"
