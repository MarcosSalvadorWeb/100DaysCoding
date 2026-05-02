from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

bank = []
for question in question_data:
    bank.append(Question(question["text"],question["answer"]))

quiz = QuizBrain(bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
