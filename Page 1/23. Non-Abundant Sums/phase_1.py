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

abundant_numbers = [number for number in range(12,28125) if number < divisors(number,True)]

n_abundant= set()
for i,number in enumerate(abundant_numbers):
    for s_number in abundant_numbers[i:]:
        if (number+s_number) > 28124: break
        n_abundant.add(number+s_number)

all_numbers = set(range(28125))
print(sum(all_numbers-n_abundant))