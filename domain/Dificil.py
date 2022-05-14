from domain.Juego import Juego


class Dificil(Juego):
    def __init__(self, nombre, puntaje):
        self.__puntaje = puntaje
        super().__init__(nombre)

    def get_puntaje(self):
        return self.__puntaje

    def set_puntaje(self, puntaje):
        self.__puntaje = puntaje

    def __str__(self):
        return super().__str__() + " " + str(self.__puntaje)
