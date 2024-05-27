def gcd(a: int,b: int): 
    if a == 0:
        return b
    return gcd(b%a,a)

def pythagorean_triplet(limit : int):
    counter = 0
    a,b,c = 1
    while counter == limit:
        if not(a < b < c):
            
