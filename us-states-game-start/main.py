from turtle import Turtle, Screen
import pandas as pd

ALIGNMENT = "center"
FONT_SIZE = 20
FONT = ("Arial", FONT_SIZE, "normal")

screen = Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
picture = Turtle().shape(image)

t = Turtle()
t.pu()
t.hideturtle()
t.speed(0)

df = pd.read_csv("50_states.csv")
n_states = len(df)


def reset_csv(dataframe):
    if not (df.columns == "complete").any():
        df["complete"] = False
    else:
        dataframe.drop(df.columns[df.columns.str.contains('complete', case=False)], axis=1, inplace=True)
        dataframe["complete"] = False
        dataframe.to_csv("50_states.csv", index=False)


# reset_csv(df)
completed_list = df.complete.to_list()
score = 0

for n in range(len(df)):
    if df.at[n, "complete"]:  # Place to take
        t.goto(int(df.at[n, "x"]), int(df.at[n, "y"]))
        t.write(df.at[n, "state"])
        score += 1

game_is_on = True
while game_is_on:

    if score >= n_states:
        t.goto(0, 260)
        t.write("Good Job! You were able to name all states in the U.S.!", align=ALIGNMENT, font=FONT)
        guess = screen.textinput(title="Start Over?", prompt="Press Y to continue.")
        if guess == "Y".lower():
            reset_csv(df)
            completed_list = df.complete.to_list()
            score = 0
            t.clear()
        else:
            game_is_on = False

    try:
        guess = screen.textinput(title=f"{score}/{n_states} States Correct",
                                 prompt="What's another state name?")
        guess = guess.title()
    except AttributeError:
        df["complete"] = completed_list
        df.to_csv("50_states.csv", index=False)
        screen.exitonclick()

    if (guess == df.state).any():
        correct_answer = df[df.state == guess]
        t.goto(int(correct_answer.x), int(correct_answer.y))
        t.write(guess)
        completed_list[correct_answer.index[0]] = True
        score += 1

screen.exitonclick()
