from Sections.Main.Prompts.MainPrompt import MainPrompt
from Sections.PrimeGenerator.PrimeGeneratorSection import PrimeGeneratorSection
from Sections.RSASetup.RSASetup import RSASetup
from Sections.RSAEncrypt.RSAEncryptSection import RSAEncryptSection
from Sections.RSADecrypt.RSADecryptSection import RSADecryptSection
from Sections.Help.HelpSection import HelpSection

class MainSection():
    def __init__(self):
        self.prompts = MainPrompt()

    def start(self):
        self.showWelcomeScreen()

        while True:
            self.prompts.show()

            continueExecution = self.startSection(self.prompts.getAnswer('section'))

            if not (continueExecution): break

    def startSection(self, id):
        if id == 1:
            PrimeGeneratorSection().start()

            return True
        elif id == 2:
            RSASetup().start()

            return True
        elif id == 3:
            RSAEncryptSection().start()

            return True
        elif id == 4:
            RSADecryptSection().start()

            return True
        elif id == 5:
            HelpSection().start()

            return True
        elif id == 6:
            print('Exit Program')

            return False

    def showWelcomeScreen(self):
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -', end = '')
        print('\n|                                                          |', end = '')
        print('\n|  Dobro dosli. Ovo je implementacija RSA kripto-sistema.  |', end = '')
        print('\n|                                                          |', end = '')
        print('\n|  Clanovi tima:                                           |', end = '')
        print('\n|      * Ema Dapcevic                                      |', end = '')
        print('\n|      * Rados Sekulovic                                   |', end = '')
        print('\n|      * Aleksa Sukovic                                    |', end = '')
        print('\n|                                                          |', end = '')
        print('\n|  Izaberite jednu od ponudjenih opcija                    |', end = '')
        print('\n|                                                          |', end = '')
        print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -\n')

