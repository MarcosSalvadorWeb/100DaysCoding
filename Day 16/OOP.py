# Em programação de objetos, queremos diminuir a complexidade do nosso código e expressar objetos de forma separada
# diminuindo assim a sobrecarga de informações e funõções.

"""
Para uma classe definimos 2 partes principais:
- Atributos (Variáveis atribuídas e pertencentes àquele objeto)
objeto.'atributo'
- Métodos (Funções do Objeto)
objeto.'method()'

Utilizamos classes para criar objetos que seriam "cópias" dos objetos
car = CarBlueprint()

Usamos letras maiúsculas em objetos
"""

from turtle import Turtle, Screen
from random import randint

Rafael = Turtle()
print(Rafael)
Rafael.shape("turtle")
Rafael.color("coral")

my_screen = Screen()
my_screen.exitonclick()