from turtle import Turtle
ALIGNMENT = "center"
FONT_SIZE = 24
FONT = ("Courier", FONT_SIZE, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(-200, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -FONT_SIZE - 10)
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
