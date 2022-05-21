from domain.Espacio import Espacio


# Clase concreta que es hereda de Espacio, por lo tanto usa los métodos y propiedades de Espacio.
class EspacioPublico(Espacio):

    # Constructor de la clase Espacio Publico.
    # Tiene dos parámetros, el primero es el lugar que ocupa y el segundo es el valor del mismo.
    def __init__(self, lugar, valor):
        super().__init__(lugar, valor)

    # Método toString de la clase Espacio Público que hereda de Object e implementa su manera de mostrar los datos.
    # Aca implementamos el polimorfismo de la clase Object
    def __str__(self):
        return "\n [Publico] Valor: " + str(self.valor) + "\n"
