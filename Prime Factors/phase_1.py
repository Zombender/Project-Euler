#600851475143

def prime_factors(number:int):
    largest_factor = 0
    divisor = 2
    while number !=1:
        if number % divisor == 0:
            print(divisor)
            number /=divisor
            largest_factor = divisor
            divisor = 2
            continue
        divisor +=1
    return largest_factor

print(f'Factor primo mas grande: {prime_factors(360)}')

