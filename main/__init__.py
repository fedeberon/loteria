from domain.EspacioPrivado import EspacioPrivado
from domain.EspacioPublico import EspacioPublico
from domain.Juego import Juego

espacio1 = EspacioPublico(1, 2)
print(espacio1)

espacio2 = EspacioPrivado(3)
print(espacio2)

juego = Juego()