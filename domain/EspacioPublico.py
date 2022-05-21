from domain.Espacio import Espacio


class EspacioPublico(Espacio):


    def __init__(self, lugar, valor):
        super().__init__(self, lugar, valor)

    def __str__(self):
        return super().__str__() + " [Publico] Valor: " + str(self.__valor)
