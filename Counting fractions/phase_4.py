'''
PHI es una funcion de euler que permite calcular la cantidad de numeros coprimos de un numero cualquiera
'''

class CountingFractions():
    fractions = 0
    def __init__(self,limit):
        self.limit = limit
        self.fract = list(range(limit+1)) # This is faster than [x for x in range(limit)] 
        self.count_fractions()

    def mcd(self,a: int,b: int): #maximo comun divisor
        if a == 0:
            return b
        return self.mcd(b%a,a)
    
    def count_fractions(self):
        for number in self.fract: #1,2,3,4
            for i in range(1,number): #iterate over number
                if self.mcd(i,number) == 1: #numero primo
                    self.fractions +=1
cf = CountingFractions(8)
print(cf.fractions)