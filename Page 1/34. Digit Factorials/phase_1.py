import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper

def is_digit_factorial(number)->bool:
    str_number = str(number)
    sum_digit_factorial = sum(MathHelper.factorial(int(digit)) for digit in str_number)
    if sum_digit_factorial == number:
        return True
    return False

numbers_digit_factorials = [number for number in range(1000000) if is_digit_factorial(number)]

print(sum(numbers_digit_factorials[2:]))
