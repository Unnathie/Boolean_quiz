class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        return self.question_no< len(self.question_list)
    def next_question(self):
        choices=input(f"Q.{self.question_no +1} {self.question_list[self.question_no].text} True/False: ").lower()
        self.checkanswer(choices,self.question_list[self.question_no].answer)
    def checkanswer(self,choices,correct):
        if choices.lower()==correct.lower():
            self.score += 1
            print(f"You were right Your score: {self.score}/{self.question_no+1}")
            self.question_no += 1
        else:
            print(f"You were Wrong Your score: {self.score}/{self.question_no+1}\nRight answer was: {self.question_list[self.question_no].answer}")
            self.question_no += 1




