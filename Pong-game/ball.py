from turtle import Turtle


class Ball(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.ball_dimension_factor = int(screen_height / (35 * 20))
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(self.ball_dimension_factor, self.ball_dimension_factor)
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1

    def move(self):
        X = self.xcor() + self.move_x
        Y = self.ycor() + self.move_y
        self.goto(X, Y)

    def bounce_off_the_walls(self):
        self.move_y = self.move_y * (-1)

    def bounce_off_the_paddle(self):
        self.move_x = self.move_x * (-1)
        self.ball_speed = self.ball_speed - 0.01
        if self.ball_speed <= 0:
            self.ball_speed = self.ball_speed + 0.01

    def re_spawn(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.move_x = self.move_x * (-1)
        self.move()
