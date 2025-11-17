from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.goto(-self.screen_width / 2.1, self.screen_height / 2.1)
        self.player_level = 1

    def score_board(self):
        self.clear()
        self.write(f"Level :{self.player_level}", font=('Courier', 10, 'bold'))

    def score_update(self):
        self.player_level = self.player_level + 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=('Courier', 40, 'bold'), align="center")
