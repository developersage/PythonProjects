from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text((150, 125), width=280,
                                            text="Some Question Text", fill="black", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        check_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=check_img, highlightthickness=0, command=self.true_press)
        self.false_button = Button(image=wrong_img, highlightthickness=0, command=self.false_press)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.display_final()

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer: bool):
        if answer:
            self.quiz.score += 1
            self.canvas.config(bg="green")
            print("You got it right!")
        else:
            self.canvas.config(bg="red")
            print("That's wrong.")

        print(f"Your current score is: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)

    def display_final(self):
        self.canvas.itemconfig(self.text, text=f"You've completed the quiz.\nYour final score was: "
                                               f"{self.quiz.score}/{self.quiz.question_number}")
