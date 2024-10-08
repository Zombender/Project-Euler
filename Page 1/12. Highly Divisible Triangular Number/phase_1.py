'''
Para calcular la cantidad de divisores de un numero cualquiera, se necesita descomponer el numero en factores primos 
Luego se suma cada potencia +1 y se multiplican entre si.

'''
def prime_factors(number:int):
    factors = []
    divisor = 2
    while number !=1:
        if number % divisor == 0:
            number /=divisor
            factors.append(divisor)
            divisor = 2
            continue
        divisor +=1
    return factors


def sum_sequence(n : int):
    return (n*(n+1))//2

def calculate_divisor(number: int):
    divisors = 1
    number_factors = prime_factors(number)
    set_factors = set(number_factors)
    for factor in set_factors:
        divisors *= number_factors.count(factor)+1
    return divisors

def calculate_divisor_limit(limit: int):
    number = 1
    while True:
        sum_ = sum_sequence(number)
        divisors = calculate_divisor(sum_)
        if divisors >=limit:
            return sum_
        number+=1

print(calculate_divisor_limit(500))
