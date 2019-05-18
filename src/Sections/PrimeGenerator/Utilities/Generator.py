from random import randrange, getrandbits
from math import floor, log

class Generator():
    """
        Generates prime number with specified length in bits
    """
    def yieldPrime(self, length = 1024, testCount = 128):
        while True:
            candidate = self._generatePrimeCandidate(length)

            if self._isPrime(candidate, testCount): return candidate

    """
        Test if given number is prime using Miller–Rabin primality test
            - 'n'         => number to check
            - 'testCount' => number of times to check
    """
    def _isPrime(self, n, testCount = 128):
        if n == 2 or n == 3: return True
        if n <= 1 or n % 2 == 0: return False

        (q, k) = self._partitionNumber(n)

        # Do required number of tests
        for f in range(testCount):
            a = randrange(2, n - 1) # potential witness
            a = pow(a, q, n)        # x = a^q mod n

            if a == 1: continue     # x^q === 1 (mod n)

            i = 0
            testPass = False

            while i < k:
                if a % n == n - 1: 
                    testPass = True
                    break

                a = pow(a, 2)
                i += 1
            
            if not testPass: return False
        
        return True
    
    """ 
        Split number n so that => n = 2^k * q
            - q is odd
    """
    def _partitionNumber(self, n):
        k = 0
        q = n - 1

        while q % 2 == 0:
            k += 1
            q //= 2

        return (q, k)
    
    """
        Generate odd random integer
            - 'length' => length of generated number in bytes
    """
    def _generatePrimeCandidate(self, length):
        number = getrandbits(length)

        number |= (1 << length - 1)
        number |= 1

        return number