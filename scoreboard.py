from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)
