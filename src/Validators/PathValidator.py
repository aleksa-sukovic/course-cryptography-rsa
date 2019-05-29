from PyInquirer import Validator, ValidationError
from pathlib import Path

class PathValidator(Validator):
    def validate(self, document):
        item = Path(document.text)

        if not item.is_file():
            raise ValidationError (
                    message = 'Molimo vas da unesete validnu putanju do datoteke.',
                    cursor_position = len(document.text)
                )
