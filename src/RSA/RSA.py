from RSA.PrimeGenerator import PrimeGenerator as Generator
from random import randrange
import math

class RSA():
    def __init__(self):
        self.primeGenerator = Generator()

    def setup(self, length = 100):
        p = self.primeGenerator.yieldPrime(length)
        q = self.primeGenerator.yieldPrime(length)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.chooseE(phi)

        gcd, x, y = self.xgcd(e, phi)
        d = x + phi if x < 0 else x

        return {
            "p": p,
            "q": q,
            "n": n,
            "phi": phi,
            "e": e,
            "d": d
        }
    
    def encrypt(self, n, e, data):
        return pow(data, e, n)

    def decrypt(self, d, n, data):
        return pow(data, d, n)

    def chooseE(self, phi):
        e = randrange(2, phi)
        
        if self.gcd(e, phi) == 1: return e

        return self.chooseE(phi)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def xgcd(self, a, b):
        x, prevX = 0, 1
        y, prevY = 1, 0

        while b != 0:
            quotient = a // b
            a, b = b, a - quotient * b          # nzd(a, b) = nzd(b, a % b)
            prevX, x = x, prevX - quotient * x  
            prevY, y = y, prevY - quotient * y

        return a, prevX, prevY