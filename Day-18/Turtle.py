from turtle import Turtle, Screen
import random as rnd
Romerio = Turtle()
Romerio.shape("turtle")
Romerio.color("coral")

def square(side):
    for i in range(4):
        Romerio.forward(side)
        Romerio.right(90)

def dash_line(size):
    for i in range(size//2):
        Romerio.forward((size*0.05)//2)
        Romerio.penup()
        Romerio.forward((size*0.05)//2)
        Romerio.pendown()


def megatragon(size, side_max = 12):
    for i in range(3,side_max+1):
        Romerio.pencolor(rnd.random(), rnd.random(), rnd.random())
        angle = 360/i
        for j in range(i):
            Romerio.forward(size)
            Romerio.right(angle)

Romerio.pensize(15)
Romerio.speed(5)
def random_walk(steps):
    directions = [0,90,180,270]
    for i in range(steps):
        choice = int(rnd.choice(directions))
        Romerio.pencolor(rnd.random(), rnd.random(), rnd.random())
        Romerio.setheading(choice)
        Romerio.forward(50)

import colorsys

def spirograph(size):
    for i in range(size):
        h = i / size
        r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
        Romerio.pencolor(r, g, b)

        Romerio.setheading(i * 360 / size)
        Romerio.circle(100)

screen = Screen()
screen.exitonclick()

import colorgram
colors = colorgram.extract('toto.jpeg',3)
first_color = colors[0]
rgb = first_color.rgb
print(rgb)