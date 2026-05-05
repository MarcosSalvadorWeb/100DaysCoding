from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 28, "bold"))

    def game_winner(self):
        self.goto(0, 0)
        self.write("GAME WINNER", align="center", font=("Courier", 28, "bold"))