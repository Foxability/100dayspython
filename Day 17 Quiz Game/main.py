from data import question_data, question_data_trivia
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data_trivia:
    question = item['question']
    correct_answer = item['correct_answer']
    question = Question(question, correct_answer)
    question_bank.append(question)

new_quiz = QuizBrain(question_bank)

new_quiz.next_question()

final_score = 0

while new_quiz.still_has_questions():
    new_quiz.next_question()

print(new_quiz.score)
