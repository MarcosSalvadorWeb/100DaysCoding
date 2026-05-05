from turtle import Turtle, Screen
import time
import random

# ---------------- TELA ---------------- #
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


# ---------------- PADDLE ---------------- #
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 25)

    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 25)


# ---------------- BALL ---------------- #
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)

        self.dx = 4
        self.dy = 4
        self.move_speed = 0.016

    def move_ball(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_wall(self):
        self.dy *= -1

    def bounce_paddle(self):
        self.dx *= -1
        self.move_speed *= 0.92  # acelera o jogo

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.016

        # manda para quem tomou o ponto
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])


# ---------------- SCORE ---------------- #
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)

        self.score_p1 = 0
        self.score_p2 = 0
        self.draw()

    def draw(self):
        self.clear()
        self.write(f"{self.score_p1}   :   {self.score_p2}",
                   align="center", font=("Courier", 20, "normal"))

    def point_p1(self):
        self.score_p1 += 1
        self.draw()

    def point_p2(self):
        self.score_p2 += 1
        self.draw()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 28, "bold"))


# ---------------- OBJETOS ---------------- #
p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

# CONTROLES
screen.listen()
screen.onkey(p1.up, "w")
screen.onkey(p1.down, "s")
screen.onkey(p2.up, "Up")
screen.onkey(p2.down, "Down")

# ---------------- LOOP ---------------- #
game_on = True
pincel1 = Turtle()
pincel1.hideturtle()
pincel1.speed(0)
pincel1.color("white")
pincel1.penup()

# ----- LINHA ESQUERDA -----
pincel1.goto(-390, 290)
pincel1.setheading(270)
pincel1.pensize(20)
pincel1.pendown()
pincel1.forward(580)
pincel1.penup()

# ----- LINHA DIREITA -----
pincel1.goto(390, 290)
pincel1.setheading(270)
pincel1.pensize(20)
pincel1.pendown()
pincel1.forward(580)
pincel1.penup()

# ----- LINHA CENTRAL TRACEJADA -----
pincel1.goto(0, 290)
pincel1.setheading(270)
pincel1.pensize(5)

for _ in range(15):
    pincel1.pendown()
    pincel1.forward(20)
    pincel1.penup()
    pincel1.forward(20)


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # teto / chão
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # colisão paddle direita
    if 320 < ball.xcor() < 350 and abs(ball.ycor() - p2.ycor()) < 50:
        ball.setx(320)
        ball.bounce_paddle()

    # colisão paddle esquerda
    if -350 < ball.xcor() < -320 and abs(ball.ycor() - p1.ycor()) < 50:
        ball.setx(-320)
        ball.bounce_paddle()

    # ponto jogador 1
    if ball.xcor() > 380:
        score.point_p1()
        ball.reset_ball()

    # ponto jogador 2
    if ball.xcor() < -380:
        score.point_p2()
        ball.reset_ball()

    # fim de jogo
    if score.score_p1 == 10 or score.score_p2 == 10:
        game_on = False
        score.game_over()

screen.exitonclick()
