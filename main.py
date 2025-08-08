from question_model import Questions
from quiz_brain import QuizBrain
from data import question_data
questionbank=[]
for ques in question_data:
    questionbank.append(Questions(ques["question"],ques["correct_answer"]))

quiz=QuizBrain(questionbank)
# for questions in questionbank:
while quiz.still_has_questions():
    quiz.next_question()
print(f"You completed the quiz! \nYOUR SCORE:{quiz.score}/{len(questionbank)}")
