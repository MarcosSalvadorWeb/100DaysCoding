from turtle import Turtle
import random as rnd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 3
DIFFICULT = 17


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(rnd.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(280, rnd.randint(-250, 250))

class CarManager():
    def __init__(self):
        self.cars = []
        self.celling = DIFFICULT
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if rnd.randint(1, self.celling) == 3:
            car = Car()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def clear_all_cars(self):
        for car in self.cars:
            car.hideturtle()
            car.goto(1000, 1000)  # garante que saiu da tela
        self.cars.clear()

    def increase_speed(self):
        self.clear_all_cars()
        self.speed += MOVE_INCREMENT

    def increase_celling(self):
        self.celling -= 1
        self.clear_all_cars()