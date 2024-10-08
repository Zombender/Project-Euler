def count_primes(limit: int ):
    number_list = list(range(2,limit))
    total = 0
    while True:
        first = number_list[0]
        total +=first
        number_list = list(filter(lambda x: x % number_list[0] !=0, number_list))
        if number_list[0]**2 < limit:   
            continue
        return sum(number_list) + total
    
print(count_primes(2000000))
