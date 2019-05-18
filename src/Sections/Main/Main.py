from Sections.Main.Prompts.MainPrompt import MainPrompt

class Main():
    def __init__(self):
        self.prompts = MainPrompt()

    def start(self):
        self.prompts.show()

        self.startSection(self.prompts.getAnswer('section'))

    def startSection(self, id):
        if id == 1:
            print('Section: Generate prime number')
        elif id == 2:
            print('Section: Initialize RSA')
        elif id == 3:
            print('Section: Encrypt')
        elif id == 4:
            print('Section: Decrypt')

