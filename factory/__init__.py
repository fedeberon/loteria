from domain.Dificil import Dificil
import logging

from domain.Dificil import Dificil
from domain.Facil import Facil


class Factory:

    @staticmethod
    def crearPartida(nivel):
        if nivel == "facil":
            return Facil()
        elif nivel == "dificil":
            return Dificil()
        else:
            logging.info('Se ingresó un nivel no valido %s', nivel)
            raise ValueError("El nivel de juego propuesto no existe. Lo siento ! :(")
