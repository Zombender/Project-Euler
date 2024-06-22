from math import factorial,prod

def sum_prize_fund(number : int):
    total_fund = 0
    steps = calculate_red_discs(number)
    for i in range(1,steps+1):
        total_fund += calculate_probabilities(i,number)
    return total_fund+1,factorial(number+1)

def calculate_probabilities(step, number):
    probabilities = 0
    total = list(range(1,step+1))
    for pos in total:
        probabilities += calculate_variants(pos, number)
    return probabilities #total is all probabilities

def calculate_red_discs(number:int):
    steps = number//2+1
    steps = number-steps
    return steps

def calculate_variants(step, number):
    if step == 1:
        return (number*(number+1))//2
    a = 1
    b = 2
    variants = []
    while a !=number:
        if b == number+1:
            a+=1
            b = a+1
        variants.append((a,b))
        b+=1
    print(variants[:-1])
    variants = list(map(lambda x : prod(x),variants[:-1]))
    return sum(variants)

num, den = sum_prize_fund(5)
print(f'{num}/{den}')
print(f'Cantidad: {num-2}')