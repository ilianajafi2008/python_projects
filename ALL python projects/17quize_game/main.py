from question_data import question_data
from quize_brain import Quize_Brain


class Question:
    def __init__(self, the_text, the_answer):
        self.text = the_text
        self.answer = the_answer


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quize = Quize_Brain(question_bank)
quize.next_question()

while quize.still_has_questions():
    quize.next_question()
    if quize.question_number == len(question_data):
        print("you've completed the quize.")
        print(f"your final score is {quize.score}/{quize.question_number}")
