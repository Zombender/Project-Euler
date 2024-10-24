import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper
is_palindrome = MathHelper.palindrome

def is_double_base_palindrome(number:int):
    binary_num = bin(number)[2:]
    if is_palindrome(str(number)) and is_palindrome(binary_num):
        return True
    return False

double_base_palindrome_numbers = [number for number in range(1,1000000) if is_double_base_palindrome(number)]
print(double_base_palindrome_numbers)
print(sum(double_base_palindrome_numbers))