import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Helpers.math_helper import MathHelper

is_prime = MathHelper.is_prime
prod = MathHelper.prod

def coeficcient_prime_chain(prime_list:list)->tuple:
    longest_prime_chain = 0
    a=0
    b=0
    for i in range(-999,1001,2):
        for j in prime_list:
            chain = prime_chain(i,j)
            if chain> longest_prime_chain:
                longest_prime_chain = chain
                a=i
                b=j
            #print(f'{a}, {b}')
    return (a,b,longest_prime_chain)

def prime_chain(a:int,b:int) ->int:
    prime_chain_count = 0
    n=0
    while True:
        result = (n**2 + a*n + b)
        if is_prime(result):
            prime_chain_count+=1
            n+=1
            continue
        return prime_chain_count
    
prime_list = [x for x in range(1,1001) if is_prime(x)]

coeficcients = coeficcient_prime_chain(prime_list)
print(coeficcients)
