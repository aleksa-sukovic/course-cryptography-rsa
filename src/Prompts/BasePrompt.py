from PyInquirer import prompt

class BasePrompt():
    def __init__(self, questions):
        self.questions = questions
    
    def show(self):
        self.answers = prompt(self.questions)

    def getAllAnswers(self):
        return self.answers

    def getAnswer(self, question):
        return self.answers[question]