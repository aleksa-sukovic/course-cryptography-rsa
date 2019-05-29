from PyInquirer import Validator, ValidationError
import regex

class NumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([0-9]|[1-9][0-9]*)$', document.text)

        if not ok:
            raise ValidationError (
                    message = 'Molimmo vas da unesete validan pozitivan broj.',
                    cursor_position = len(document.text)
                )