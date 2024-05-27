def smallest_multiple(limit : int):
    list_numbers = list(range(1,limit))
    number = limit
    while all_divisibility(list_numbers,number) == False:
        number +=limit
    return number

def all_divisibility(list_numbers:list,number:int):
    for num in list_numbers:
        if number % num !=0:
            return False
    return True

num = smallest_multiple(20)
print(num)