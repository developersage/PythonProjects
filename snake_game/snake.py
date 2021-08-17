from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

SCREEN_X = 280
SCREEN_Y = 280
MOVE_DISTANCE = 20


class Snake:
    snake = []
    position = []

    def __init__(self, n=1):
        self.create_snake(n)
        self.head = self.snake[0]
        self.head.color("grey")

    def create_snake(self, n):
        for i in range(n):
            self.position.append((-MOVE_DISTANCE * i, 0))
            self.add_body(self.position[i])

    def add_body(self, pos):
        obj = Turtle("square")
        obj.pu()
        obj.color("white")
        obj.goto(pos)
        self.snake.append(obj)

    def extend(self):
        self.add_body(self.snake[-1].position())

    def move(self):
        for idx in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[idx - 1].xcor()
            new_y = self.snake[idx - 1].ycor()
            self.snake[idx].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def is_bumped_to_body(self):
        for each_body in self.snake[1:]:
            if self.head.distance(each_body) < 10:
                return True
        return False

    def is_bumped_to_x_wall(self):
        return self.head.xcor() > SCREEN_X or self.head.xcor() < -SCREEN_X

    def is_bumped_to_y_wall(self):
        return self.head.ycor() > SCREEN_Y or self.head.ycor() < -SCREEN_Y

    def reset(self):
        for body in self.snake:
            body.color("black")
        self.snake.clear()
        self.__init__(n=3)
