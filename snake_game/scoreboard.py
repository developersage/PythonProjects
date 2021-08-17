from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 20
FONT = ("Arial", FONT_SIZE, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        try:
            with open("data.txt", mode="r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError or ValueError:
            self.high_score = 0
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.pu()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -FONT_SIZE - 10)
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
