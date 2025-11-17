from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(0, -screen_height / 2.1)
        self.move_y = 10

    def move_up(self):
        Y = self.ycor() + self.move_y
        self.goto(0, Y)
