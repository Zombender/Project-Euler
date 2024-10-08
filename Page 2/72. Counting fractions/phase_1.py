'''
Positive Keys:
    If d is Prime, then fraction is unique
    If the sum of d and n results in prime number, the fraction is unique
Negative Keys:
    If d and n can be divided, they are not unique
'''
from functools import reduce

def prime_condition(number : int):
    for x in range(2, (number//2)+1):
        if number % x == 0:
            return False,x
    return True

def sum_condition(number : int): #True = prime, false = not prime
    return True if prime_condition(number) else False

def divide_condition(denominador :int, numerador: int):

    pass
    
class Fractions():
    counting = 0
    def __init__(self, limit):
        self.limit = limit
        self.fractions = []
        self.create_fractions()
    def create_fractions(self):
        d = 2
        while d < self.limit+1:
            if prime_condition(d):
                self.counting +=d-1
                self.fractions.append([f'{num}/{d}' for num in range(1,d)])
                d+=1
                continue
            list_fraction = []
            for x in range(1,d):
                if not sum_condition(d+x):
                    continue
                list_fraction.append(f'{x}/{d}')
                self.counting +=1
            self.fractions.append(list_fraction)
            d+=1

fract = Fractions(8)
print(fract.counting)
print(fract.fractions)



