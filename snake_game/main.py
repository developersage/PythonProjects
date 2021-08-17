from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sage's Snake Game")
screen.tracer(0)

snake = Snake(10)
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.inc_score()

    # Detect collision with its own tail
    if snake.is_bumped_to_body():
        score.reset()
        snake.reset()

    # # Detect collision with a wall
    # if snake.is_bumped_to_x_wall() or snake.is_bumped_to_y_wall():
    #     game_is_on = False
    #     score.game_over()

    # Make an infinite space when colliding to a wall
    if snake.is_bumped_to_x_wall():
        snake.head.setx(-snake.head.xcor())
    if snake.is_bumped_to_y_wall():
        snake.head.sety(-snake.head.ycor())

screen.exitonclick()
