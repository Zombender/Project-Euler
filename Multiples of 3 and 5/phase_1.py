class Multiples3And5:
    def __init__(self,limit):
        self.limit = limit
        self.numbers = list(range(limit))
        self.new_numbers = self.counting_multiples()
    def counting_multiples(self):
        new_numbers = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, self.numbers))
        return new_numbers
    

instance = Multiples3And5(1000)
print(sum(instance.new_numbers))