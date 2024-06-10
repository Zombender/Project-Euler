def sum_amicable_numbers():
    total = 0
    proven_numbers = set()
    for a in range(1,10000):
        if a in proven_numbers:continue
        b = d(a)
        if a == d(b) and b == d(a) and a!=b:
            proven_numbers.add(a)
            proven_numbers.add(b)
    return proven_numbers
        

def d(number:int):
    max_factor = int(number **0.5)
    factors = []
    for i in range(1,max_factor+1):
        if number %i == 0:
            factors.append(i)
            factors.append(int(number/i))
    return sum(set(filter(lambda x : x<=number//2,factors)))


print(sum_amicable_numbers())
