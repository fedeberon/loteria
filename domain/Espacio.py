from abc import ABC


class Espacio(ABC):

    __ubicacion: int

    ## Constructor de la clase Espacio
    def __init__(self, ubicacion):
        self.__ubicacion = ubicacion

    ## Getters y Setters de la clase Espacio
    def getUbicacion(self):
        return self.__ubicacion

    def setUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def __str__(self):
        return "[UBICACION]: " + str(self.__ubicacion)
