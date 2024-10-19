import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper

from copy import deepcopy

#limits: 1000,99999

number_list = [str(number) for number in range(1,10)]

def filter_numbers(number: str,number_list:list)->bool:
    for n in number:
        if n not in number_list:
            return False
        number_list.remove(n)
    return True

def pandigital_number(number,number_list)->bool:
    divisors = list(MathHelper.d(number))
    divisors = [divisor for divisor in divisors if 1<=divisor<=9999]
    for i in range(len(divisors)):
        for j in range(i+1,len(divisors)):
            temp_list = deepcopy(number_list)
            if not filter_numbers(str(divisors[i]),temp_list): continue #filters i divisor
            if not filter_numbers(str(divisors[j]),temp_list): continue #filters j divisor
            if not divisors[i] * divisors[j] == number: continue #verifies that this combination equals number
            if not temp_list : #Verifies that list is empty
                print(f'{divisors[i]} * {divisors[j]} = {number}//{temp_list}')
                return True
    return False
def pandigitals_numbers():
    pandigital_list = set()
    for i in range(0,10000):
    #for i in range(6952,6953 ):
        temp_list = deepcopy(number_list)
        if not filter_numbers(str(i),temp_list):
            continue
        if pandigital_number(i,temp_list):
            pandigital_list.add(i)
    return pandigital_list

set_pandigital = pandigitals_numbers()
print(sum(set_pandigital))