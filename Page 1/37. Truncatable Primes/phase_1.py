import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper

is_prime = MathHelper.is_prime

def is_truncatable_prime_both_sides(number:str):
    left_truncatable = number
    right_truncatable = number
    if len(number) == 1:
        return False
    while True:
        if not is_prime(int(left_truncatable)):
            return False
        if len(left_truncatable) == 1: 
            break
        left_truncatable = truncate_number(left_truncatable,'left')
    while True:
        if not is_prime(int(right_truncatable)):
            return False
        if len(right_truncatable)==1:
            return True
        right_truncatable = truncate_number(right_truncatable,'right')

def truncate_number(number:str,order):
    if order == 'left':
        return number[1:]
    elif order == 'right':
        return number[:-1]

truncatable_prime_list = list()
number = 1
while len(truncatable_prime_list) !=11:
    truncatable_prime_list.append(number) if is_truncatable_prime_both_sides(str(number)) else None
    number+=1
print(truncatable_prime_list)
print(f'Sum: {sum(truncatable_prime_list)}')