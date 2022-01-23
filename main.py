import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def exit_game():
    screen.bye()


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(exit_game, "Escape")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.car_move()
    screen.update()

    if player.distance(car_manager) <= 25:
        player.car_crash()
        scoreboard.score = 1
        scoreboard.update_score()

    if player.ycor() >= player.finish_line:
        player.reached_end()
        scoreboard.score += 1
        scoreboard.update_score()

screen.exitonclick()
