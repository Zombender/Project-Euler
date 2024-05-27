#600851475143

def prime_factors(number:int):
    largest_factor = 0
    divisor = 2
    while number !=1:
        if number % divisor == 0:
            number /=divisor
            largest_factor = divisor
        divisor +=1
    return largest_factor

print(prime_factors(580085))

