from PyInquirer import prompt
import sys

class BasePrompt():
    def __init__(self, questions):
        self.questions = questions
    
    def show(self):
        print()
        
        self.answers = prompt(self.questions)

        if not self.hasRequiredAnswers(self.answers): sys.exit()

    def showSingle(self, prompt):
        print()

        self.answers = prompt(prompt)

        if not self.hasRequiredAnswers(self.answers): sys.exit()

    def getAllAnswers(self):
        return self.answers

    def getAnswer(self, question):
        if not hasattr(self, 'answers') or not question in self.answers: 
            sys.exit()
        
        return self.answers[question]

    def hasRequiredAnswers(self, answers):
        return True
