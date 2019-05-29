from Prompts.BasePrompt import BasePrompt
from Validators.NumberValidator import NumberValidator
from Validators.WritePathValidator import WritePathValidator
from PyInquirer import prompt
from Validators.PathValidator import PathValidator
import sys

class RSAEncryptPrompt(BasePrompt):
    def __init__(self):
        super(RSAEncryptPrompt, self).__init__(({
            'type': 'input',
            'name': 'n',
            'message': 'Unesite N:',
            'validate': NumberValidator
        }, {
            'type': 'input',
            'name': 'e',
            'message': 'Unesite E:',
            'validate': NumberValidator
        }, {
            'type': 'list',
            'name': 'outputType',
            'message': 'Da li zelite da sacuvate enkriptovan sadrzaj unutar datoteke ?',
            'choices': [
                { 'name': '1) Da', 'value': 1 },
                { 'name': '2) Ne', 'value': 2 }
            ]
        }, {
            'type': 'list',
            'name': 'source',
            'message': 'Da li zelite da unesete sadrzaj iz datoteke ili preko tastature ?',
            'choices': [
                { 'name': '1) Tastatura', 'value': 1 },
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

        return answer['inputPath'] if 'inputPath' in answer else sys.exit()

    def showContentPrompt(self):
        answer = prompt(({
            'type': 'input',
            'name': 'content',
            'message': 'Unesite sadrzaj za enkripciju:'
        }))

        return answer['content'] if 'content' in answer else sys.exit()

    def showOutputPathPrompt(self):
        answer = prompt(({
            'type': 'input',
            'name': 'outputPath',
            'message': 'Unesite putanju do fajla u koji zelite snimiti:',
            'validate': WritePathValidator
        }))

        return answer['outputPath'] if 'outputPath' in answer else sys.exit()

    def hasRequiredAnswers(self, answers):
        hasRequired = True
        hasRequired = hasRequired and 'n' in answers
        hasRequired = hasRequired and 'e' in answers
        hasRequired = hasRequired and 'outputType' in answers
        hasRequired = hasRequired and 'source' in answers
        return hasRequired
