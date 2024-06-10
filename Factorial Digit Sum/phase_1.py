def factorial(number: int):
    result = 1
    for num in range(1, number+1):
        result *=num
    return result

def factorial_digit_sum(number: int):
    factorial_number = factorial(number)
    total_digit_sum = sum(int(digit) for digit in str(factorial_number))
    return total_digit_sum

print(factorial_digit_sum(100))