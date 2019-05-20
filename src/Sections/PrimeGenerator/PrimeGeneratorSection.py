from Sections.PrimeGenerator.Prompts.PrimeGeneratorPrompt import PrimeGeneratorPrompt
from RSA.PrimeGenerator import PrimeGenerator

class PrimeGeneratorSection():
    def start(self):
        generator = PrimeGenerator()
        prompts = PrimeGeneratorPrompt()
        prompts.show()

        length = int(prompts.getAnswer('length'))
        count = int(prompts.getAnswer('count'))

        print()
        for i in range(count):
            print('     {}) {}'.format(i + 1, generator.yieldPrime(length)))

