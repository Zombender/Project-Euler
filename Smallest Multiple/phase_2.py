
def gcd(a: int,b: int): 
    if a == 0:
        return b
    return gcd(b%a,a)

def lcd(a: int, b:int):
    return a*b // gcd(a,b)

def smallest_multiple(limit : int):
    sm = 1
    for i in range(1,limit):
        sm = lcd(sm, i)
    return sm

print(smallest_multiple(20))
