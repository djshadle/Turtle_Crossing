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
scoreboard = Scoreboard()
time_counter = 5

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(exit_game, "Escape")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    time_counter += 1
    screen.update()

    if time_counter % 6 == 0:
        car_manager = CarManager()
    car_manager.car_move()
    # if player.distance(car_manager) <= 25:
    #     player.car_crash()
    #     scoreboard.score = 1
    #     scoreboard.update_score()
    #
    # if player.ycor() >= player.finish_line:
    #     player.reached_end()
    #     scoreboard.score += 1
    #     scoreboard.update_score()
    #     car_manager.speed_up()


screen.exitonclick()
