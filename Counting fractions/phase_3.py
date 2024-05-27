'''
Positive Keys:
    If d is prime, then fraction is unique
Negative Keys:
    If n is a d's divisor, fraction is not unique
'''

class CountingFractions():
    fractions = 0
    def __init__(self,limit):
        self.limit = limit
        self.count_fractions()
    
    def is_prime_number(self, number: int):
        for i in range (2,(number//2)+1):
            if number % i == 0:
                return False
        return True
    
    def divisors(self, number: int):
        return [i for i in range(2,(number//2)+1) if number %i == 0]

    
    def has_divisor(self,number: int, divisors : list):
        for divisor in divisors:
            if number % divisor == 0: return True
        return False

    def count_fractions(self):
        d=2
        while d < self.limit+1:
            print(f'number: {d} --- counting: {self.fractions}')
            if self.is_prime_number(d):
                self.fractions += d-1
                d+=1
                continue
            self.fractions+=1 #Este viene de cualquier fraccion con numerador 1 y denominador 'd'
            divisors = self.divisors(d)
            print(f'divisors: {divisors}')
            for i in range(2,d):
                if self.has_divisor(i,divisors): continue# if i has divisor...
                self.fractions +=1
            d+=1    

count = CountingFractions(254)
print(count.fractions)