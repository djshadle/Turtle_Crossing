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

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(exit_game, "Escape")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1

    if counter % 6 == 0:
        car_manager = CarManager()
        cars.append(car_manager)

    for car in cars:
        if car.xcor() < -310:
            cars.remove(car)
        car.forward(car_manager.car_speed)

        if player.distance(car) <= 25:
            player.car_crash()
            scoreboard.score = 1
            scoreboard.update_score()

    if player.ycor() >= player.finish_line:
        player.reached_end()
        scoreboard.score += 1
        scoreboard.update_score()
        car_manager.speed_up()

screen.exitonclick()
