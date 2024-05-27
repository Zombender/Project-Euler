class CountingFractions():
    fractions = 0
    def __init__(self,limit):
        self.limit = limit
        self.fract = list(range(limit+1)) # This is faster than [x for x in range(limit)] 
        self.count_fractions()

    def count_fractions(self):
        for i in range(2, self.limit+1):
            print(self.fract)
            if self.fract[i] == i: #prime number
                for j in range(i, self.limit+1,i): # saltos de i en i en el rango de self.limit
                    self.fract[j] *= (i - 1) # i-1 representa la cantidad de divisores de un numero primo
                    self.fract[j] //= i # Propiedad multiplicativa
        self.fractions += sum(self.fract[2:])

cf = CountingFractions(8)
print(cf.fractions)