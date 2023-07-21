from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()
        self.correct_position()

    def refresh(self):
        self.hideturtle()
        random_x = random.randrange(-240, 240, 20)
        random_y = random.randrange(-220, 220, 20)
        self.goto(random_x, random_y)

    def correct_position(self):
        self.showturtle()
