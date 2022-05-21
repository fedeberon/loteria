from domain.EspacioPublico import EspacioPublico
from factory import Factory

# Iniciamos el juego.
print("Bienvenido al juego de la vida!")

# Pedimos el nivel de juego al jugador.
nivel = input("Ingrese el nivel de juego [dificil - facil]: ")

# Creamos la instancia de la clase Factory que se encarga de definir la logica del nivel de juego.
factory = Factory(nivel)

# Obtenemos la instancia de la clase según el nivel ingresado por el usuario.
juego = factory.crearPartida(nivel)

# Ingresamos los espacios públicos propuestos por el jugador.
# TODO Falta tomar los datos de Jugador
juego.ingresarEspacios([EspacioPublico(1, 1), EspacioPublico(2, 2)])

# Obtenemos la cantidad de espacios ingresados por el jugador.
cantidadDeEspaciosACompletar = len(juego.cantidadDeEspacios)

# Preguntamos al Jugador los números que desea ingresar.
espaciosIngresados = input(f"Ingrese {cantidadDeEspaciosACompletar} números")

# Mostramos todos los datos de juego
print(juego)
