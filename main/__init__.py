from domain.Dificil import Dificil
from domain.EspacioPublico import EspacioPublico
from domain.Facil import Facil


def crearPartida(nivel):
    if nivel == "facil":
        return Facil()
    elif nivel == "medio":
        return "medio"
    elif nivel == "dificil":
        return Dificil()
    else:
        return "error"


print("Bienvenido al juego de la vida!")
nivel = input("Ingrese el nivel de juego [dificil - facil]: ")

juego = crearPartida(nivel)
juego.ingresarEspacios([EspacioPublico(1, 1), EspacioPublico(2, 2)])
cantidadDeEspaciosACompletar = len(juego.getEspacios())

espaciosIngresados = input(f"Ingrese {cantidadDeEspaciosACompletar} numeros")


print(juego)
