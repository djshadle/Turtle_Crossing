import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def exit_game():
    screen.bye()


counter = 0
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(exit_game, "Escape")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()

    car_manager.movement()
    car_manager.remove_car()
    # Detect collision with player
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            player.car_crash()
            game_is_on = False
            scoreboard.game_over()

    # Detect player at finish line
        if player.reached_finish_line():
            scoreboard.score += 1
            scoreboard.update_score()
            car_manager.level_up()

screen.exitonclick()
