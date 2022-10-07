class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        guess = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)? ")
        self.check_answer(guess)
        self.still_has_questions()
        self.question_number += 1

    def check_answer(self, guess):
        if guess == self.question_list[self.question_number].answer:
            self.score += 1
            print(f"You got it right! \nThe correct answer was: {self.question_list[self.question_number].answer}. "
                  f"\nYour current score is: {self.score}/{self.question_number+1}")
        else:
            print(f"Wrong answer! \nThe correct answer was: {self.question_list[self.question_number].answer}. "
                  f"\nYour current score is: {self.score}/{self.question_number+1}")
        print("\n")
