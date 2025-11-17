from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("square")
        self.color("white")
        self.penup()
        self.left(90)
        self.paddle_width_factor = screen_width / 2400
        self.paddle_height_factor = screen_height / 175
        self.shapesize(self.paddle_width_factor, self.paddle_height_factor)
        self.paddle_position = -screen_width/2 + 10
        self.goto(self.paddle_position, 0)

    def up(self):
        if self.ycor() + (self.paddle_height_factor * 20)/2 < self.screen_height / 2:
            self.forward(20)

    def down(self):
        if -self.ycor() + (self.paddle_height_factor * 20)/2 < self.screen_height / 2:
            self.back(20)
