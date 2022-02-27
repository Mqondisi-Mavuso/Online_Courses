from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# a list that will contain the question objects which will have question and answer
question_bank = []

for question in question_data:
    q_text = question["question"]           # assigning the question to the q_text
    q_answer = question["correct_answer"]       # assigning the question from the question_data list
    question_obj = Question(q_text, q_answer)  # constructing the question object using the two variables from above
    question_bank.append(question_obj)          # appending the object to the question bank list

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score is {quiz.score}/{len(quiz.q_list)}")