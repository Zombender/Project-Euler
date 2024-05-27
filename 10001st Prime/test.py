def prime_condition(number : int):
    for x in range(2, (number//2)+1):
        if number % x == 0:
            return False,x
    return True,x

print(prime_condition(13))