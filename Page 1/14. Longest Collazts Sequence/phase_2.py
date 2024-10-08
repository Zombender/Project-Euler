def collatz_sequence(number):
    list_c = []
    list_c.append(number)
    while number !=1:
        if number %2 == 0:
            number //=2
        else:
            number = number*3 +1
        list_c.append(number)
    return list_c
            
for x in range(1,17):
    print(collatz_sequence(x))