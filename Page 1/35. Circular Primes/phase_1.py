import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper

is_prime = MathHelper.is_prime

def is_circular_prime(number:int)->bool:
    str_number = str(number)
    rotated_number = str_number
    while True:
        if not is_prime(int(rotated_number)): return False
        if len(str_number)==1: return True

def rotate_number(number:str)->str:
    for i,digit in enumerate(number):
        pass
    #continue here

