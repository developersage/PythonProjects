import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

CAR_AMOUNT = 20
TIME_SPEED = 0.05

cars = CarManager(CAR_AMOUNT)
user = Player()
score = Scoreboard()

screen.listen()
screen.onkey(user.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(TIME_SPEED)
    screen.update()
    cars.move()

    if user.is_finished():
        score.inc_score()
        TIME_SPEED *= 0.9

    if cars.is_hit(user):
        score.game_over()
        game_is_on = False

screen.exitonclick()
