import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper


def list_digit_cancel_fractions()->list:
    fractions = list()
    numbers = [number for number in range(10,100)]
    for i in range(1,len(numbers)):
        for j in range(i,len(numbers)):
            result = numbers[i]/numbers[j]
            if result >= 1: continue
            if numbers[i] %10 == 0 and numbers[j] %10 == 0: continue
            if check_equality(numbers[i],numbers[j],result):
                fractions.append((numbers[i],numbers[j]))
    return fractions

def check_equality(n1,n2,result)->bool:
    n1 = str(n1)
    n2 = str(n2)
    equal_numbers = list(set(n1) & set(n2))
    if not equal_numbers:
        return False
    n1 = [n for n in n1 if n not in equal_numbers]
    n2 = [n for n in n2 if n not in equal_numbers]
    n1 = int(''.join(n1) if n1 else 0)
    n2 = int(''.join(n2) if n2 else 0)
    if n2 == 0:
        return False
    if result == n1/n2:
        return True
list_fractions = list_digit_cancel_fractions()

numerator = MathHelper.prod(list(fraction[0] for fraction in list_fractions))
denominator = MathHelper.prod(list(fraction[1] for fraction in list_fractions))

gcd = MathHelper.gcd(numerator,denominator)

numerator/=gcd
denominator/=gcd

print(numerator, denominator)
    