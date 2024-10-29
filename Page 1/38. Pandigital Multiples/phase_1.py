

def pandigital_concatenated_product(number:int)->str|None:
    concatenated_number = str(number)
    n=2
    while True:
        is_pandigital_number = is_pandigital(concatenated_number)
        if is_pandigital_number is False:
            return None
        elif is_pandigital_number is True:
            return concatenated_number
        concatenated_number += str(number*n)
        n+=1
        
def is_pandigital(number:str)->bool|str:
    one_to_nine:str = ''.join([str(num) for num in range(1,10)])
    number = ''.join(sorted(number))
    len_number:int = len(number)
    if len_number < 9:
        return 'i'
    #incomplete, you need to iterate to find out if its pandigital
    elif len_number > 9:
        return False
    if one_to_nine == number:
        return True
    return False

pandigital_contatenated_product_list = [pandigital_concatenated_product(number) 
                                        for number in range(1,10001)
                                        if pandigital_concatenated_product(number) != None]

pandigital_contatenated_product_list = list(filter(lambda x: x!=None,pandigital_contatenated_product_list))

pandigital_contatenated_product_list.sort(key=int,reverse=True)

print(pandigital_contatenated_product_list[0])