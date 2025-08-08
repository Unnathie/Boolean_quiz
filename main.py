from question_model import Questions
from quiz_brain import QuizBrain
from data import question_data,funfact_data
questionbank=[]
choices=int(input("Choose your quiz mode:\nPress 1 for Fun Facts.\nPress 2 for Trivia Challenge."))
if choices==1:
    for ques in funfact_data:
        questionbank.append(Questions(ques["text"],ques["answer"]))

else:
    for ques in question_data:
        questionbank.append(Questions(ques["question"], ques["correct_answer"]))



quiz=QuizBrain(questionbank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You completed the quiz! \nYOUR SCORE:{quiz.score}/{len(questionbank)}")
