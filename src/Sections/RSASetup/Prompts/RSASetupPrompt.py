from Prompts.BasePrompt import BasePrompt
from Validators.NumberValidator import NumberValidator

class RSASetupPrompt(BasePrompt):
    def __init__(self):
        super(RSASetupPrompt, self).__init__(({
            'type': 'input',
            'name': 'length',
            'message': 'Duzina broja (u bitima):',
            'validate': NumberValidator
        }))

    def hasRequiredAnswers(self, answers):
        hasRequired = True
        hasRequired = hasRequired and 'length' in answers
        return hasRequired