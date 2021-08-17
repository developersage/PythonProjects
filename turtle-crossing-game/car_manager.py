from turtle import Turtle
from random import Random
import math
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FULL_X = 600
FULL_Y = 600
HALF_X = FULL_X / 2 - 40
HALF_Y = FULL_Y / 2 - 40


class CarManager:

    def __init__(self, n_of_cars):
        self.cars = []
        self.r = Random()
        for _ in range(n_of_cars):
            obj = Turtle("square")
            obj.pu()
            obj.color(self.r.choice(COLORS))
            obj.shapesize(stretch_wid=1, stretch_len=2)
            obj.seth(180)
            obj.speed_value = self.r.randint(STARTING_MOVE_DISTANCE, MOVE_INCREMENT)
            x = self.r.randrange(-HALF_X, HALF_X, 10)
            y = self.r.randrange(-HALF_Y, HALF_Y, 40)
            obj.goto(x, y)
            self.cars.append(obj)

    def move(self):
        for car in self.cars:
            if car.xcor() > -HALF_X:
                car.forward(car.speed_value)
            else:
                car.goto(HALF_X, self.r.randrange(-HALF_Y, HALF_Y, 10))
                car.speed_value = self.r.randint(STARTING_MOVE_DISTANCE, MOVE_INCREMENT)

    def is_hit(self, obj):
        for car in self.cars:
            if math.isclose(car.xcor(), obj.xcor(), abs_tol=20) and \
                    math.isclose(car.ycor(), obj.ycor(), abs_tol=10):
                return True
        return False
