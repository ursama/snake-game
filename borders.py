from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        # Right Border
        self.create_border((270, 250), 270, 500)
        # Left Border
        self.create_border((-270, 250), 270, 500)
        # Top Border
        self.create_border((-270, 250), 0, 540)
        # Down Border
        self.create_border((-270, -250), 0, 540)

    def create_border(self, position, heading, forward):
        border = Turtle()
        border.color("orange")
        border.hideturtle()
        border.pensize(width=2)
        border.penup()
        border.goto(position)
        border.pendown()
        border.setheading(heading)
        border.forward(forward)
