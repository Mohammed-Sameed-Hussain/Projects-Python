import time
from turtle import Screen
from my_turtle import MyTurtle
from car_fleet import CarFleet
from scoreboard import ScoreBoard

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = Screen()
screen.listen()
screen.title("Turtle Crossing Capstone")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

screen.tracer(0)
my_turtle = MyTurtle(SCREEN_HEIGHT)
scoreboard = ScoreBoard(SCREEN_HEIGHT, SCREEN_WIDTH)
scoreboard.score_board()
screen.update()

carFleet = CarFleet(SCREEN_HEIGHT, SCREEN_WIDTH)

game_is_on = True
while game_is_on:
    time.sleep(carFleet.timedelay)
    screen.onkey(my_turtle.move_up, "Up")
    if len(carFleet.fleet_of_cars) <= 30:
        carFleet.create_car()
    carFleet.move_car()

    # Detect Collision
    for car in carFleet.fleet_of_cars:
        if car.distance(my_turtle) < (10 + (20 * (SCREEN_HEIGHT / 800)) / 2):
            scoreboard.game_over()
            game_is_on = False

    # Detect the turtle has reached the other end
    if my_turtle.ycor() >= SCREEN_HEIGHT / 2.1:
        my_turtle.goto(0, -SCREEN_HEIGHT / 2.1)
        carFleet.timedelay = carFleet.timedelay - carFleet.time_decrement
        print(carFleet.timedelay)
        scoreboard.score_update()

    screen.update()

screen.exitonclick()
