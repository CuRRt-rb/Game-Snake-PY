from turtle import Turtle
POSITIONING = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_creation()
        self.head = self.segments[0]

    def snake_creation(self):
        for position in POSITIONING: # Creating a body
            self.adding(position)


    def adding(self, position):
        snake = Turtle("square")
        snake.color("black")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)


    def extension(self):
        self.adding(self.segments[-1].position())

    def move(self):
        for s_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s_number - 1].xcor()
            new_y = self.segments[s_number - 1].ycor()
            self.segments[s_number].goto(new_x, new_y)
        self.head.forward(MOVEMENT)

    def up(self): #Movement
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)