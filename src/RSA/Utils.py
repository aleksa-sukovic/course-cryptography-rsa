class Utils():
    def gcd(self, a, b):
        while True:
            temp = a % b
            if temp == 0:
                return b
            a = b
            b = temp