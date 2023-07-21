from turtle import Screen
from borders import Border
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
border = Border()

snake = Snake()
food = Food()
score = Scoreboard()


def main():
    playing_game = True
    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

    score.write_score()

    while playing_game:

        # Moving continuously
        snake.move()
        screen.update()
        time.sleep(0.07)

        # Detect collision with food
        errors = True
        if snake.head.distance(food) < 17:
            score.got_point()
            if len(snake.squares) <= 150:
                snake.add_square()
            while errors:
                errors = False
                food.refresh()
                for square in snake.squares:
                    if square.distance(food) < 10:
                        errors = True
            food.correct_position()

        # Detect collision with wall
        if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 220 or snake.head.ycor() < -220:
            score.high_score_update()
            playing_game = False
            score.game_over()

        # Detect collision with tail
        for square in snake.squares[1:]:
            if snake.head.distance(square) < 10:
                playing_game = False
                score.high_score_update()
                score.game_over()

        # Determine if player wants to play again
        if not playing_game:
            screen.onkeypress(reset, "y")
            screen.onkeypress(screen.bye, "n")

    screen.exitonclick()


def reset():
    snake.reset()
    main()


if __name__ == "__main__":
    main()
