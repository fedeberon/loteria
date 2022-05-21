import names
import random
import logging

from domain.EspacioPrivado import EspacioPrivado
from domain.Juego import Juego


# Clase concreta que es hereda de Juego, por lo tanto usa los métodos y propiedades de Juego.
class Facil(Juego):

    # Constructor de la clase Faácil. Definimos un nombre random a modo de ejemplo de usuario.
    def __init__(self):
        self.__nombre = names.get_full_name()

    # Método que se encarga de ingresar los espacios públicos.
    # Aca implementamos el polimorfismo de la clase Juego, ya que solo implementa DOS espacios públicos.
    def ingresarEspacios(self, espacio_publico):
        logging.info('Ingresando los espacios públicos %s', espacio_publico)
        self.espacioPrivado = [
            EspacioPrivado(1, random.randrange(0, 101)),
            EspacioPrivado(2, random.randrange(0, 101)),
        ]
        self.espacioPublico = espacio_publico

    # Método toString de la clase Facil que hereda de Object e implementa su manera de mostrar los datos.
    # Aca implementamos el polimorfismo de la clase Object
    def __str__(self):
        return self.__nombre + " - Nivel Fácil" \
               + " - Números Ingresados " + self.getDatosIngresados() \
               + " - Números Propuestos por el Juego " + self.getDatosPropuestos()
