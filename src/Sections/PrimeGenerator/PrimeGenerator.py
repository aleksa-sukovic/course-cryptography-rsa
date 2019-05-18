from Sections.PrimeGenerator.Prompts.PrimeGeneratorPrompt import PrimeGeneratorPrompt
from Sections.PrimeGenerator.Utilities.Generator import Generator

class PrimeGenerator():
    def start(self):
        generator = Generator()
        prompts = PrimeGeneratorPrompt()
        prompts.show()

        length = int(prompts.getAnswer('length'))
        count = int(prompts.getAnswer('count'))

        print()
        for i in range(count):
            print('     {}) {}'.format(i + 1, generator.yieldPrime(length)))

