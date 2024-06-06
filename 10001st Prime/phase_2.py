def is_prime(number:int):
    if number == 1:return False
    elif number  < 4: return True
    elif number %2 == 0: return False
    elif number <9 : return True
    elif number %3 == 0: return False
    sqr = round(number**0.5)
    f= 5
    while f <= sqr:
        if number % f == 0: return False
        if number % (f+2) == 0: return False
        f+=6
    return True

def prime_position(position:int):
    prime_number = 1
    i = 0
    while i !=position-1:
        prime_number+=2
        if is_prime(prime_number):
            i+=1
    return prime_number


print(prime_position(4))


