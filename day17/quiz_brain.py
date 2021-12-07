
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.right_answered = 0
        self.attempts = 0

    def next_question(self):
        self.question_number += 1
        self.attempts += 1
        cur_question = self.question_list[self.question_number-1]
        user_answer = input(f"Q.{self.question_number}: {cur_question.text} (True/False)?:").capitalize()
        if user_answer == cur_question.answer:
            self.right_answered += 1
            print("You got it right!\n"
                  f"The correct answer was: {cur_question.answer}\n"
                  f"Your current score is: {self.right_answered}/{self.attempts}")
        else:
            print("Wrong!\n"
                  f"The correct answer was: {cur_question.answer}\n"
                  f"Your current score is: {self.right_answered}/{self.attempts}")
        if self.question_number == len(self.question_list):
            print("\nGame is over\n"
                  f"Your result is: {self.right_answered}/{len(self.question_list)}")
            self.question_number = 0
        else:
            self.next_question()
