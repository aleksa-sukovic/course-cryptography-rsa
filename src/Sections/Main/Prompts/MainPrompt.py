from Prompts.BasePrompt import BasePrompt

class MainPrompt(BasePrompt):
    def __init__(self):
        super(MainPrompt, self).__init__(({
            'type': 'list',
            'name': 'section',
            'message': 'Sta zelite da uradite?',
            'choices': [
                { 'name': 'Generisi prost broj zeljene duzine', 'value': 1 },
                { 'name': 'Inicijalizuj RSA sistem', 'value': 2 },
                { 'name': 'Enkriptuj podatke', 'value': 3 },
                { 'name': 'Prikazi pomoc', 'value': 4 }
            ]
        }))