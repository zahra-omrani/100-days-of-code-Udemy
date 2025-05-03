from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0,len(question_data)):
    question_text = question_data[i]['text']
    question_answer = question_data[i]['answer']
    question_instance = Question(question_text,question_answer)
    question_bank.append(question_instance)

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()