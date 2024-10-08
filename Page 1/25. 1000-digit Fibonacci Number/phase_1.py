def F(number_digits):
    index = 1
    n,n_2 = 0,1
    while len(str(n)) <number_digits:
        n,n_2 = n_2,n+n_2
        index+=1
    return index-1

print(F(1000))