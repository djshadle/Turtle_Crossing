from turtle import Turtle
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.random_chance = 6

    def create_car(self):
        rand_int = random.randint(1, self.random_chance)
        if len(self.all_cars) < 22 and rand_int == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def remove_car(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                self.all_cars.remove(car)

    def movement(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.random_chance != 4:
            self.random_chance -= 2
        elif self.random_chance != 1:
            self.random_chance -= 1

