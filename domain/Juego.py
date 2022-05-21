from abc import abstractmethod, ABC


class Juego(ABC):
    __nombre: str
    __espacioPublico: list
    __espacioPrivado: list

    @property
    def cantidadDeEspacios(self):
        return len(self.__espacio_privado)

    @abstractmethod
    def ingresarEspacios(self, espacios):
        pass
