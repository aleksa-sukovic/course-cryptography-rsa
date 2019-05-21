from RSA.RSA import RSA
from Sections.RSADecrypt.Prompts.RSADecryptPrompt import RSADecryptPrompt

class RSADecryptSection():
    def start(self):
        self.rsa = RSA()
        self.prompts = RSADecryptPrompt()

        self.showPrompts()
        self.decrypt()

    def showPrompts(self):
        self.prompts.show()

        # get data
        self.n = int(self.prompts.getAnswer('n'))
        self.d = int(self.prompts.getAnswer('d'))
        self.source = int(self.prompts.getAnswer('source'))
        self.outputType = self.prompts.getAnswer('outputType')

        # read from keyboard
        if self.source == 1:
            self.content = self.prompts.showContentPrompt()

        # read from file
        if self.source == 2:
            path = self.prompts.showInputPathPrompt()
            with open(path) as fileContent:
                self.content = fileContent.read()

        # get output file path
        if self.outputType == 1:
            self.outputPath = self.prompts.showOutputPathPrompt()

    def decrypt(self):
        # generate decrypted content
        data = self.content.split(' ')
        output = ''

        for item in data:
            output += chr(self.rsa.decrypt(self.d, self.n, int(item)))

        # generate output
        if self.outputType == 1:
            f = open(self.outputPath, 'w')
            f.write(output)

        # print result
        print()
        print('Decrypted content:')
        print()
        print(output)

