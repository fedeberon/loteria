from abc import abstractmethod, ABC


# Clase abstracta desde donde se
# definen los comportamientos comunes a todos los juegos
class Juego(ABC):
    nombre: str
    espacioPublico: list
    espacioPrivado: list

    # Propiedad que es resuelve una acción commún a todos los juegos
    @property
    def cantidadDeEspacios(self):
        return self.espacioPrivado

    def getDatosIngresados(self):
        return ''.join(str(e) for e in self.espacioPublico)

    def getDatosPropuestos(self):
        return ''.join(str(e) for e in self.espacioPrivado)

    @abstractmethod
    def ingresarEspacios(self, espaciosPublicos, espacioPrivado):
        pass

    def __str__(self):
        return self.nombre