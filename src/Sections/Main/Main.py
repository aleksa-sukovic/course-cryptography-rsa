from Sections.Main.Prompts.MainPrompt import MainPrompt

class Main():
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
            print('Section: Generate prime number')

            return True
        elif id == 2:
            print('Section: Initialize RSA')

            return True
        elif id == 3:
            print('Section: Encrypt')

            return True
        elif id == 4:
            print('Section: Decrypt')

            return True
        elif id == 5:
            print('Exit program')

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

