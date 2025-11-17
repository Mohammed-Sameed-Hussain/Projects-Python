from turtle import Screen
import time
from splitscreen import SplitScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# splitting the screen
screen.tracer(0)
split_screen = SplitScreen(SCREEN_HEIGHT)
screen.update()

# creating the paddles
paddle_1 = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)
print(paddle_1.position())
screen.update()

paddle_2 = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)
paddle_2.paddle_position = -paddle_1.paddle_position
paddle_2.goto(paddle_2.paddle_position, 0)
# paddle_2.goto(-list(paddle_2.position())[0], list(paddle_2.position())[1])
print(paddle_2.position())
screen.update()

# giving keyboard commands
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

ball = Ball(SCREEN_HEIGHT)
score_board = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)
score_board.score_board()

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Detecting Collision With the upper and lower wall
    if ball.ball_dimension_factor * 20 + ball.ycor() > SCREEN_HEIGHT / 2 or \
            ball.ycor() - ball.ball_dimension_factor * 20 < -SCREEN_HEIGHT / 2:
        ball.bounce_off_the_walls()

    # Detecting collision with the right_paddle
    if abs(paddle_2.xcor() - ball.xcor()) <= (
            paddle_2.paddle_width_factor + ball.ball_dimension_factor) * 10 and abs(paddle_2.ycor() - ball.ycor()) <= (
            ball.ball_dimension_factor + paddle_2.paddle_height_factor) * 10:
        ball.bounce_off_the_paddle()
    # Detecting collision with the left_paddle
    if abs(paddle_1.xcor() - ball.xcor()) <= (
            paddle_1.paddle_width_factor + ball.ball_dimension_factor) * 10 and abs(paddle_1.ycor() - ball.ycor()) <= (
            ball.ball_dimension_factor + paddle_1.paddle_height_factor) * 10:
        ball.bounce_off_the_paddle()
    # Detecting no Collision with the paddle
    if ball.xcor() >= SCREEN_WIDTH / 2:
        ball.re_spawn()
        score_board.score_update_right()
    elif ball.xcor() <= -SCREEN_WIDTH / 2:
        ball.re_spawn()
        score_board.score_update_left()

screen.exitonclick()
