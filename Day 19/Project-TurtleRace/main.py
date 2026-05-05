import random
import turtle
from turtle import Screen,Turtle

COLORS = ["red","orange","yellow","green","blue"]
WIDTH = [-100,-50,0,50,100]
all_turtles = []
for i in range(0,5):
    tim = Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(COLORS[i])
    tim.goto(-250,WIDTH[i])
    all_turtles.append(tim)

screen = Screen()
screen.setup(width=600,height=400)
screen.colormode(255)
guess = screen.textinput("BET", "QUAL A COR DA TARTARUGA QUE VENCERÁ A CORRIDA? ")
racer = True
while racer:
    for t in all_turtles:
        if t.xcor() > 250:
            racer = False
            winning_color = t.color()[0]
            if winning_color == guess:
                print(f"You guessed right {winning_color} is the Winner!")
                break
            else:
                print(f"You guessed wrong {winning_color} is the Winner!")
                break
        else:
            dd = random.randint(0, 10)
            t.forward(dd)

screen.exitonclick()

#SKETCH-UP
""""
def move_foward(size=10):
    timmy.forward(size)
def move_backward(size=10):
    timmy.backward(size)
def counter_clockwise(angle=5):
    timmy.left(angle)
def clockwise(angle=5):
    timmy.right(angle)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.onkey(key = "s", fun = move_backward)
screen.onkey(key="w",fun=move_foward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="q",fun=clear)

screen.exitonclick()
"""
