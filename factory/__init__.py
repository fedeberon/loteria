from domain import Juego
from domain.Dificil import Dificil
from domain.Facil import Facil
import logging

class Factory:
    __nivel: Juego

    def __init__(self, nivel):
        self.__nivel = nivel

    def crearPartida(nivel):
        if nivel == "facil":
            return Facil()
        elif nivel == "dificil":
            return Dificil()
        else:
            logging.info('Se ingresó un nivel no valido %s', nivel)
            raise ValueError("El nivel de juego propuesto no existe. Lo siento ! :(")
