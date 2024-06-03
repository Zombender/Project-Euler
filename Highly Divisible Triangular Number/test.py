
def gcd(a: int,b: int): 
    if a == 0:
        return b
    return gcd(b%a,a)

def lcd(a: int, b:int):
    return a*b // gcd(a,b)
