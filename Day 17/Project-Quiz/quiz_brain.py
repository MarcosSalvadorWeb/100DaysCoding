class QuizBrain:
    def __init__(self,questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        n = len(self.questions_list)
        return(self.question_number < n-1)

    def next_question(self):
        current = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {self.questions_list[self.question_number].text} (True/False)?")
        self.check_answer(user_answer,self.questions_list[self.question_number].answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Correct Answer: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print()