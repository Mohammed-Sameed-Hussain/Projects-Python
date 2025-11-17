import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
snake_food = Food()
my_score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()
    if snake.my_snake[0].distance(snake_food) <= 6:
        snake_food.consumed()
        my_score.increment_score()
        snake.increase_length()

    if snake.my_snake[0].xcor()>=296 or snake.my_snake[0].xcor()<=-296 or snake.my_snake[0].ycor()>=296 or snake.my_snake[0].ycor()<=-296 :
        # game_is_on= False
        my_score.reset()
        snake.reset_snake()
    for snake_segments in snake.my_snake[1::]:
        if snake.my_snake[0].distance(snake_segments) < 4:
            # game_is_on = False
            my_score.reset()
            snake.reset_snake()

screen.exitonclick()
