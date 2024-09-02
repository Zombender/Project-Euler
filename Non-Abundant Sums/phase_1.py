def divisors(number:int, sum_ = False) -> set | int:
    max_factor = int(number **0.5)
    factors = []
    for i in range(1,max_factor+1):
        if number %i == 0:
            factors.append(i)
            factors.append(int(number/i))
    factors = set(filter(lambda x : x<=number//2,factors))
    if sum_:
        return sum(factors)
    return factors

abundant_numbers = [number for number in range(28124) if number < divisors(number,True)]
def abundant_index(number:int) ->int:
    for i,abundant_number in enumerate(abundant_numbers):
        if abundant_number > number:
            return i
def two_abundant_sum(number:int) -> bool:
    index = len(abundant_numbers)
    for i in range(index):
        if i > number: continue
        for j in range(i,index):
            if j > number: break
            if abundant_numbers[i] + abundant_numbers[j] == number: return True
    return False
#non_abundant_numbers = [number for number in range(1,28124) if not two_abundant_sum(number)]
non_abundant_numbers = []
for i in range(1,28124):
    if not two_abundant_sum(i):
        non_abundant_numbers.append(i)
        print(i)
print(sum(non_abundant_numbers))
