class EvenFibonacci():
    def __init__(self):
        self.sequence = [0,1]
        self.fibonacci()
    def fibonacci(self):
        x=1
        while True:
            next = self.sequence[x-1]+self.sequence[x]
            if next >=4000000:break
            self.sequence.append(next)
            x+=1
    def even_fibonacci(self):
        evens = list(filter(lambda x: x % 2== 0,self.sequence))
        return sum(evens)
    
instance = EvenFibonacci()
print(instance.even_fibonacci())

#This code can be improved