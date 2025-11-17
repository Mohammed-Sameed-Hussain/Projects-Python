from turtle import Turtle

RELATIVE_SIZE_TURTLE = 0.4
SNAKE_STEP = int(RELATIVE_SIZE_TURTLE * 20)


class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            my_turtle = Turtle("square")
            my_turtle.color("white")
            my_turtle.shapesize(RELATIVE_SIZE_TURTLE, RELATIVE_SIZE_TURTLE)
            my_turtle.penup()
            my_turtle.setx(-SNAKE_STEP * i)
            self.my_snake.append(my_turtle)

    def move(self):
        for turtles_num in range(len(self.my_snake) - 1, 0, -1):
            self.my_snake[turtles_num].goto(self.my_snake[turtles_num - 1].xcor(),
                                            self.my_snake[turtles_num - 1].ycor())
        self.my_snake[0].forward(8)

    def increase_length(self):
        for i in range(0, 3):
            my_turtle = Turtle("square")
            my_turtle.color("white")
            my_turtle.shapesize(RELATIVE_SIZE_TURTLE, RELATIVE_SIZE_TURTLE)
            my_turtle.penup()
            my_turtle.goto(self.my_snake[-1].position())
            self.my_snake.append(my_turtle)

    def reset_snake(self):
        for segments in self.my_snake:
            segments.goto(2000, 2000)
        self.my_snake.clear()
        self.create_snake()

    def up(self):
        if int(self.my_snake[0].heading()) == 0:
            self.my_snake[0].left(90)
        elif int(self.my_snake[0].heading()) == 180:
            self.my_snake[0].right(90)

    def down(self):
        if int(self.my_snake[0].heading()) == 0:
            self.my_snake[0].right(90)
        elif int(self.my_snake[0].heading()) == 180:
            self.my_snake[0].left(90)

    def right(self):
        if int(self.my_snake[0].heading()) == 90:
            self.my_snake[0].right(90)
        elif int(self.my_snake[0].heading()) == 270:
            self.my_snake[0].left(90)

    def left(self):
        if int(self.my_snake[0].heading()) == 90:
            self.my_snake[0].left(90)
        elif int(self.my_snake[0].heading()) == 270:
            self.my_snake[0].right(90)
