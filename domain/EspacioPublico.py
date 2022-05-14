from domain.Espacio import Espacio


class EspacioPublico(Espacio):
    __valor = 0

    def __init__(self, valor, ubicacion):
        self.__valor = valor
        super().__init__(ubicacion)

    def setValor(self, valor):
        self.__valor = valor

    def getValor(self):
        return self.__valor

    def __str__(self):
        return super().__str__() + " [Publico] Valor: " + str(self.__valor)
