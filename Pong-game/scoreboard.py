from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.r_player = 0
        self.l_player = 0
        self.penup()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height

    def score_board(self):
        self.clear()
        self.goto(x=-self.SCREEN_WIDTH / 4, y=self.SCREEN_HEIGHT / 2.5)
        self.write(self.r_player, font=('Courier', 40, 'bold'))
        self.goto(x=self.SCREEN_WIDTH / 4, y=self.SCREEN_HEIGHT / 2.5)
        self.write(self.l_player, font=('Courier', 40, 'bold'))

    def score_update_right(self):
        self.r_player = self.r_player + 1
        self.score_board()

    def score_update_left(self):
        self.l_player = self.l_player + 1
        self.score_board()
