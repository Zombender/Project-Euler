'''
    This can be used for longest_recyprocal_cycle, but is less efficient 

    cycle_longitude_number_list = [cycle_longitude(numerator,denominator) for denominator in range(1,denominator_limit+1)]
    return cycle_longitude_number_list.index(max(cycle_longitude_number_list))

'''
def longest_recyprocal_cycle(numerator,denominator_limit:int):
    max_ = 0
    max_index = 0
    for denominator in range(1,denominator_limit+1):
        cycle_value = cycle_longitude(numerator,denominator)
        if cycle_value > max_:
            max_ = cycle_value
            max_index = denominator-1
    return max_index

def cycle_longitude(numerator: int, denominator: int) -> int:
    module_map = {}
    if numerator < denominator:
        numerator *= 10
    index = 0
    while True:
        while numerator < denominator:
            numerator *= 10
        module_number = numerator % denominator
        if module_number == 0:
            return 0 
        if module_number in module_map:
            return index - module_map[module_number] 
        module_map[module_number] = index
        numerator = module_number * 10 
        index += 1

numerator = 1
denominator = 11
denominator_limit = 10000
print(longest_recyprocal_cycle(numerator,denominator_limit)+1)

