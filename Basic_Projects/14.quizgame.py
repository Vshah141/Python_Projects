class Question():

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain():

    def __init__(self, q_list):
        self.ques_number = 0
        self.score = 0
        self.ques_list = q_list

    def still_has_ques(self):
        if self.ques_number < len(self.ques_list):
            return True
        else:
            return False

    def next_ques(self):
        current_ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        answer = input(
            f"Q. {self.ques_number}:{current_ques.text} (True/False):")
        self.check_ans(answer, current_ques.answer)

    def check_ans(self, username, answer):

        if username.lower() == answer.lower():
            print("Right")
            self.score += 1
            print(f"Your current score is {self.score}/{self.ques_number}")
        else:
            print("Wrong")
            self.score += 0
            print(f"Your current score is {self.score}/{self.ques_number}")


question_data = [
    {"text": "My name is Vyom", "answer": "True"},
    {"text": "I am 17 years old", "answer": "False"},
    {"text": "I am studying engineering", "answer": "True"}
]
question_bank = []
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_ques = Question(q_text, q_ans)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_ques()
