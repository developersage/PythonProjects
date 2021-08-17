from question_model import Question
from data import q_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for q in q_data["results"]:
    new_question = Question(q["question"], q["correct_answer"])
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
