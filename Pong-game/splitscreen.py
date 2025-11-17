from turtle import Turtle


class SplitScreen(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.split_bar_density = 46
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, -self.screen_height / 2 + 10)
        self.left(90)
        self.width(3)
        self.split_screen()

    def split_screen(self):
        for i in range(0, int(self.split_bar_density / 2)):
            self.pendown()
            self.forward(self.screen_height / self.split_bar_density)
            self.penup()
            self.forward(self.screen_height / self.split_bar_density)
