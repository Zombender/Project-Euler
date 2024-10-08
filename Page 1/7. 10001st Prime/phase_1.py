def prime_condition(number : int):
    for x in range(2, (number//2)+1):
        if number % x == 0:
            return False
    return number


def position_prime_number(position:int):
    prime = 0
    i = 0
    index = 0
    while index !=position+2:
        if prime_condition(i) ==i :
            prime = i
            index+=1
        i+=1
    return prime

print(position_prime_number(10001))
        