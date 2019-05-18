from PyInquirer import prompt

class BasePrompt():
    def __init__(self, questions):
        self.questions = questions
    
    def show(self):
        print()
        self.answers = prompt(self.questions)

    def getAllAnswers(self):
        return self.answers

    def getAnswer(self, question):
        if not hasattr(self, 'answers') or not question in self.answers: 
            return None
        
        return self.answers[question]
