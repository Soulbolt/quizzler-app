import html

class QuizBrain:
    # Add attributes -> question_number = 0 and questions_list
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        user_answer = input(f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False)\n").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
