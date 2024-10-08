'''
n/2 if n is even
3n+1 if n is odd

'''
def longest_collatz_sequence(limit: int):
    number_dict = {}
    start = 1
    while start != limit:
        key, value = collatz_sequence(start,number_dict)
        number_dict[key] = value
        start +=1
    return max(number_dict, key=number_dict.get)
def collatz_sequence(number, number_dict : dict):
    original_number = number
    quantity = 0
    while number !=1:
        if number %2 == 0:
            number //=2
        else:
            number = number*3 +1
        quantity +=1
        if number in number_dict.keys(): #you already have the quantity
            quantity += number_dict[number]
            return original_number, quantity
    return original_number, quantity

print(longest_collatz_sequence(1000000))
        

    