from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.setheading(180)
        self.create_car()

    def car_move(self):
        while True:
            self.forward(self.car_speed)

    def create_car(self):
        self.goto(310, (random.randint(-250, 250)))
        self.car_move()

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
