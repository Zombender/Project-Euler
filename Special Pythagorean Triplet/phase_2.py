
'''
u = square odd integer
v = double the square of an integer

a = sqr(2uv)+u
b = sqr(2uv)+v
c = sqr(2uv)+u+v

GCD(u,v) = 1 # u and v are coprimes
'''
from time import sleep
def gcd(a: int,b: int): 
    if a == 0:
        return b
    return gcd(b%a,a)

def u_ (odd_integer:int):
    return odd_integer **2

def v_ (integer:int):
    return (integer**2) * 2

def define_triplet(u : int, v : int) ->tuple:

    a = (2*u*v)**0.5 + u
    b = (2*u*v)**0.5 + v
    c = (2*u*v)**0.5 + u + v
    return (int(a), int(b), int(c))

def generated_triplet(values : tuple, found: int):
    x = 1
    while True:
        a,b,c = values[0]*x, values[1]*x,values[2]*x
        total = sum((a,b,c,))
        if total > found:
            break
        elif total == found:
            return (a,b,c)
        x+=1
    return False
def calculate_pythagorean_triplets(found: int):
    u_c = 1
    v_c = 1
    while True:
        for value in range(1,u_c): #calculate for u
            u = u_(u_c) # 
            v = v_(value) #
            if gcd(u,v) !=1:
                continue    
            triplet = generated_triplet(define_triplet(u,v),found)
            if triplet !=False:
                return triplet
        for value in range(1,v_c): #calculate for v
            u = u_(value)
            v = v_(v_c)
            if gcd(u,v) !=1:
                continue
            triplet = generated_triplet(define_triplet(u,v),found)
            if triplet !=False:
                return triplet
        u = u_(u_c) # 1
        v = v_(v_c) # 2
        if gcd(u,v) !=1: #not coprime
            u_c+=1
            v_c+=1
            continue
        triplet = generated_triplet(define_triplet(u,v),found)
        if triplet !=False:return triplet
        u_c +=1
        v_c+=1
        
triplet = calculate_pythagorean_triplets(1000)
total = 1
for value in triplet:
    total *=value
print(total)




            
