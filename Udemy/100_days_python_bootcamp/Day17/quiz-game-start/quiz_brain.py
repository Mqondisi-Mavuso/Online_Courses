class QuizBrain:

    def __init__(self, q_list):
        """
        This is the default constructor that will construct the object during declaration time
        :param q_list: takes the question list parameter and constructs the object
        """
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        """
        prompts the user for true or false until all the questions have been answered
        :return: No return value
        """
        try:
            current_question = self.q_list[self.q_number]
        except:
            print("Index out of range")
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}:{current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        checks the length of the list of questions and returns true if there
        are still questions to be answered and false if there are no more questions left
        :return: True or False boolean
        """
        return self.q_number < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's incorrect")
        print(f"The correct answer was {correct_answer}")
        print(f" Current score is {self.score}/ {self.q_number} ")
        print("\n")
