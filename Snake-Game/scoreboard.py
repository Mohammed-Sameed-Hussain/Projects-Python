from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"My Score: {self.score}    High Score: {self.high_score}", False, "center", ('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))
            self.increment_score()
        self.score = 0
        self.clear()
        self.write(f"My Score: {self.score}    High Score: {self.high_score}", False, "center", ('Arial', 15, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, "center", ('Arial', 20, 'normal'))

    def increment_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"My Score: {self.score}    High Score: {self.high_score}", False, "center", ('Arial', 15, 'normal'))
