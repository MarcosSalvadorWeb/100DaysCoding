import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
manager = CarManager()
player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    manager.create_car()
    manager.move_cars()

    if player.ycor() >= 280:
        player.reset_position()
        manager.increase_speed()
        scoreboard.update()
        if scoreboard.level%3 == 0:
            manager.increase_celling()

    for car in manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if game_is_on and scoreboard.level == 10:
        scoreboard.game_winner()

screen.exitonclick()