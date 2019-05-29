from Sections.RSASetup.Prompts.RSASetupPrompt import RSASetupPrompt
from RSA.RSA import RSA

class RSASetup():
    def __init__(self):
        self.prompts = RSASetupPrompt()

    def start(self):
        self.prompts = RSASetupPrompt()
        self.prompts.show()

        length = int(self.prompts.getAnswer('length'))

        self.showOutput(RSA().setup(length))

    def showOutput(self, values):
        print("     p  => {}".format(values['p']))
        print("     q  => {}".format(values['q']))
        print("     n  => {}".format(values['n']))
        print("     fi => {}".format(values['phi']))
        print("     e  => {}".format(values['e']))
        print("     d  => {}".format(values['d']))
        print("     Par (n, e) cini vas javni kljuc ({}, {})".format(values['n'], values['e']))
        print("     Vas privatni kljuc je (d) ({})".format(values['d']))