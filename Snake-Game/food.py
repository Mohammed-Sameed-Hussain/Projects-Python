from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.color("blue")
        self.speed(0)
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)
        self.consumed()

    def consumed(self):
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)
