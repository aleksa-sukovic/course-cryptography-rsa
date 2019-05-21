from PyInquirer import Validator, ValidationError
from pathlib import Path

class WritePathValidator(Validator):
    def validate(self, document):
        try:
            fileHandle = open(document.text, 'w')
        except FileNotFoundError:
            raise ValidationError (
                    message = 'Molimo vas da provjerite zadatu putanju.',
                    cursor_position = len(document.text)
                )
