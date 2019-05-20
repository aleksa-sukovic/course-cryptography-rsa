from Prompts.BasePrompt import BasePrompt

class MainPrompt(BasePrompt):
    def __init__(self):
        super(MainPrompt, self).__init__(({
            'type': 'list',
            'name': 'section',
            'message': 'Sta zelite da uradite?',
            'choices': [
                { 'name': '1) Generisi prost broj zeljene duzine', 'value': 1 },
                { 'name': '2) Inicijalizuj RSA sistem', 'value': 2 },
                { 'name': '3) Enkriptuj podatke', 'value': 3 },
                { 'name': '4) Dekriptuj podatke', 'value': 4 },
                { 'name': '5) Prikazi pomoc', 'value': 5 },
                { 'name': '6) Napusti program', 'value': 6 }
            ]
        }))