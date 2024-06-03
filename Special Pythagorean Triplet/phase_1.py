
'''
u = square odd integer
v = double the square of an integer

a = sqr(2uv)+u
b = sqr(2uv)+v
c = sqr(2uv)+u+v

GCD(u,v) = 1 # u and v are coprimes

a , b , c
a^2+b^2=c^2
a<b<c

3^2+4^2 = 5^2
'''
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

def calculate_pythagorean_triplets(limit : int):
    triplets = []
    u_c = 1
    v_c = 1
    while len(triplets) < limit:
        for value in range(1,u_c): #calculate for u
            u = u_(u_c) # 
            v = v_(value) #
            if gcd(u,v) !=1:
                continue    
            triplets.append(define_triplet(u,v))
        for value in range(1,v_c): #calculate for v
            u = u_(value)
            v = v_(v_c)
            if gcd(u,v) !=1:
                continue
            triplets.append(define_triplet(u,v))
        u = u_(u_c) # 1
        v = v_(v_c) # 2
        if gcd(u,v) !=1: #not coprime
            u_c+=1
            v_c+=1
            continue
        triplets.append(define_triplet(u_(u_c),v_(v_c)))
        u_c +=1
        v_c+=1
    return triplets
        
print(calculate_pythagorean_triplets(8))


            
