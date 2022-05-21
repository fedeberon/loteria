from abc import abstractmethod, ABC


class Juego(ABC):
    __nombre: str
    __espacioPublico: list
    __espacioPrivado: list

    @abstractmethod
    def cantidadDeEspacios(self):
        pass

    @abstractmethod
    def ingresarEspacios(self, espacios):
        pass
