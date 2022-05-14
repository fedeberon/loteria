from domain.Juego import Juego


class Facil(Juego):
    def __init__(self, nombre, dificultad, tiempo, puntaje):
        self.__dificultad = dificultad
        self.__tiempo = tiempo
        self.__puntaje = puntaje
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " - Nivel Facil"


