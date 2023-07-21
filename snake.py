from turtle import Turtle

SIZE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.squares = []
        self.squares_reserve = []
        self.create_snake()
        self.head = self.squares[0]
        self.head.shape('circle')
        self.head.color('gold')
        self.head.shapesize(0.8, 0.9)

    def reset(self):
        for square in self.squares:
            square.reset()
            # square.goto(-1000, -1000)
            # self.squares.remove(square)
            # self.squares_reserve.append(square)
        self.squares.clear()
        self.__init__()

    def create_snake(self):
        for start_size in range(0, 3):
            self.add_square()

    def add_square(self):
        # if self.squares_reserve:
        #     square = self.squares_reserve.pop()
        # else:
        square = Turtle()

        if len(self.squares) % 5 == 0:
            square.color("goldenrod")
        else:
            square.color("dark goldenrod")

        square.shape("square")
        square.shapesize(1, 1)
        square.penup()

        self.squares.append(square)
        if len(self.squares) == 1:
            self.squares[0].goto(0, 0)
        else:
            index = self.squares.index(square)
            self.squares[index].setx(self.squares[index - 1].xcor() - SIZE)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_xcor = self.squares[square_num - 1].xcor()
            new_ycor = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_xcor, new_ycor)
        self.head.forward(SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


if __name__ == "__main__":
    pass
