import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.penup()
        self.shape("square")
        self.left(180)
        self.shapesize(stretch_wid=screen_height / 800, stretch_len=screen_height / 400)
        self.move_x = -2
        self.color(random.choice(COLORS))
        Y = random.uniform(-(screen_height / 2 - 80), screen_height / 2 - 80)
        self.goto(screen_width / 2, Y)

    def move(self):
        X = self.xcor() + self.move_x
        self.setx(X)
        self.regenerate()

    def regenerate(self):
        if self.xcor() < -self.screen_width / 2 - ((20 * (self.screen_height / 400)) / 2):
            self.color(random.choice(COLORS))
            Y = random.uniform(-(self.screen_height / 2 - 80), self.screen_height / 2 - 80)
            self.goto(self.screen_width / 2, Y)
