from question_model_1 import Question
from data import question_data
from question_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    obj_question = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(obj_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    #quiz.check_answer(user_answer = , correct_answer=)

print("You've completed the quiz")
print(f"Yor final score was {quiz.score}/{quiz.question_number}")

# to get the questions from the other/new questions
# use Open Trivia Database