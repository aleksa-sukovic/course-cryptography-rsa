from PyInquirer import prompt
from Prompts.BasePrompt import BasePrompt
from Validators.NumberValidator import NumberValidator
from Validators.WritePathValidator import WritePathValidator
from Validators.PathValidator import PathValidator

class RSADecryptPrompt(BasePrompt):
    def __init__(self):
        super(RSADecryptPrompt, self).__init__(({
            'type': 'input',
            'name': 'n',
            'message': 'Unesite N:',
            'validate': NumberValidator
        }, {
            'type': 'input',
            'name': 'd',
            'message': 'Unesite D (privatni kljuc):',
            'validate': NumberValidator
        }, {
            'type': 'list',
            'name': 'outputType',
            'message': 'Da li zelite da sacuvate dekriptovan sadrzaj unutar datoteke ?',
            'choices': [
                { 'name': '1) Da', 'value': 1 },
                { 'name': '2) Ne', 'value': 2 }
            ]
        }, {
            'type': 'list',
            'name': 'source',
            'message': 'Da li zelite da unesete cypher sadrzaj iz datoteke ili preko tastature ?',
            'choices': [
                { 'name': '1) Tastatura (svaki karakter je odvojen jednim blankom)', 'value': 1 },
                { 'name': '2) Datoteka', 'value': 2 }
            ]
        }))

    def showInputPathPrompt(self):
        answer = prompt(({
            'type': 'input',
            'name': 'inputPath',
            'message': 'Unesite putanju do datoteke iz koje zelite procitati sadrzaj:',
            'validate': PathValidator
        }))

        return answer['inputPath'] if 'inputPath' in answer else quit()

    def showContentPrompt(self):
        answer = prompt(({
            'type': 'input',
            'name': 'content',
            'message': 'Unesite sadrzaj za enkripciju:'
        }))

        return answer['path'] if 'path' in answer else quit()

    def showOutputPathPrompt(self):
        answer = prompt(({
            'type': 'input',
            'name': 'outputPath',
            'message': 'Unesite putanju do fajla u koji zelite snimiti dekriptovan sadrzaj:',
            'validate': WritePathValidator
        }))

        return answer['outputPath'] if 'outputPath' in answer else quit()

    def hasRequiredAnswers(self, answers):
        hasRequired = True
        hasRequired = hasRequired and 'n' in answers
        hasRequired = hasRequired and 'd' in answers
        hasRequired = hasRequired and 'outputType' in answers
        hasRequired = hasRequired and 'source' in answers
        return hasRequired