from domain import Juego
from domain.Dificil import Dificil
from domain.Facil import Facil


class Factory:
    __nivel: Juego

    def __init__(self, nivel):
        self.__nivel = nivel

    def crearPartida(self):
        if self.__nivel == "facil":
            return Facil()
        elif self.__nivel == "medio":
            return "medio"
        elif self.__nivel == "dificil":
            return Dificil()
        else:
            return "error"
