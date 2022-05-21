import names

from domain.EspacioPrivado import EspacioPrivado
from domain.Juego import Juego


class Dificil(Juego):

    def ingresarEspacios(self, espacio_publico):
        super().__espacioPrivado = [EspacioPrivado(1),
                                    EspacioPrivado(2),
                                    EspacioPrivado(3),
                                    EspacioPrivado(4),
                                    EspacioPrivado(5)]
        super().__espacioPublico = espacio_publico

    def __init__(self):
        self._nombre = names.get_full_name()

    def __str__(self):
        return self._nombre + " - Nivel Dificil"
