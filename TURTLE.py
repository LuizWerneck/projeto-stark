############### Primeiros passos ############################################

import turtle            # permite usar as funções e objetos do módulo turtle
wn = turtle.Screen()     # cria uma janela gráfica
alex = turtle.Turtle()   # cria um turtle chamado alex
alex.forward(150)        # manda o alex se mover 150 unidades para frente
alex.left(90)            # roda de 90 graus para a esquerda
alex.forward(75)         # desenha o segundo lado do retângulo

#################### Mover tartaruga ########################################

from turtle import *
shape("turtle")
speed(5)

forward(100)
right(90)
forward(100)

done()

#############################################################################

from turtle import *
shape("turtle")
speed(8)

color("Purple")
pensize(7)
right(90)
forward(100)
left(90)
forward(50)

color("Orange")
pensize(3)
penup()
forward(50)
pendown()
forward(50)

done()

####################### Quadrado #############################################

from turtle import *

speed(11)
shape("turtle")

for count in range(4):
    forward(100)
    right(90)

done()

## octogono #################################################################

from turtle import *

speed(11)
shape("turtle")

for count in range(8):
    forward(100)
    right(45)

done()

######################### circulo ##########################################

from turtle import *

speed(11)
shape("classic")

for count in range(360):
    forward(1)
    right(1)

done()

############################################################################

from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Green")

for count in range(36):
    forward(100)
    right(100)

done()

################ Estipulando variavel para desenhar ########################

from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Green")
lados = 6
angulo = 360 / lados

for count in range(lados):
    forward(angulo)
    left(angulo)

done()

############### E com INPUT #################################################

from turtle import *

lados_1 = input ('Insira o número de lados: ')
lados = int(lados_1)
angulo = 360 / lados

speed(11)
shape("turtle")
pensize(4)
color("Green")

for count in range (lados):
    forward(angulo)
    left(angulo)

done()