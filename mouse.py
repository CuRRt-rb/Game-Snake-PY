from turtle import Turtle
import random

class Mouse(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.restart()


    def restart(self):
        random_a = random.randint(-380, 380)
        random_b = random.randint(-380, 380)
        self.goto(random_a, random_b)
