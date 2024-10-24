import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper

is_prime = MathHelper.is_prime

def is_circular_prime(number:int)->bool:
    str_number = str(number)
    if not is_prime(number): return False
    if len(str_number)==1: return True
    rotated_number = rotate_number(str_number)
    while True:
        prime = is_prime(int(rotated_number))
        if not prime: 
            return False
        if rotated_number == str_number: 
            return True
        rotated_number = rotate_number(rotated_number)

def rotate_number(number:str)->str:
    if len(number) == 1: return number
    return ''.join([number[i-1] for i in range(len(number))])

circular_prime_list = [number for number in range(3,1000000,2) if is_circular_prime(number)]
print(circular_prime_list)
print(f'Quantity: {len(circular_prime_list)+1}')
