from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        with open("data.txt", mode='w+') as file:
            data = file.read()
            if not data:
                file.write("0")
                data = "0"
            self.high_score = int(data)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def got_point(self):
        self.score += 1
        self.write_score()

    def reset_game(self):
        pass

    def high_score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write(f"Final score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, -60)
        self.write(f"Do you want to continue? y/n", align=ALIGNMENT, font=FONT)
        self.goto(0, 260)
        self.score = 0
