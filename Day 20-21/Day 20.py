import time
from turtle import Screen, Turtle
import random as rnd
from scipy.datasets import download_all

screen = Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title(titlestring="SNAKE GAME")
screen.tracer(0)


initial_length = 3
move_distance = 17
Positions = [(0,0),(-20,0),(-40,0)]


class Snake:
    def __init__(self):
        self.initial_length = initial_length
        self.move_distance = move_distance
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.size = len(self.segments)

    def create_snake(self):
        for position in Positions:
            self.add_segment(position)

    def add_segment(self,position):
        new = Turtle()
        new.penup()
        new.color("white")
        new.shape("square")
        new.goto(position)
        self.segments.append(new)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            position_x = self.segments[seg - 1].xcor()
            position_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(position_x, position_y)
        self.segments[0].forward(self.move_distance)
    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def eat(self):
        new = Turtle()
        new.penup()
        new.color("white")
        new.shape("square")
        self.segments.append(new)



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = rnd.randint(-270,270)
        random_y = rnd.randint(-270,270)
        self.goto(random_x, random_y)

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))
        self.hideturtle()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

snake = Snake()
screen.listen()
food = Food()
scoreboard = scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:snake.size]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()



screen.exitonclick()