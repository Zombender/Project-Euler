def calculate_sum(number, exponent):
    result = pow(number,exponent)
    result = str(result)
    result_sum = sum(int(x) for x in result)
    return result_sum
print(calculate_sum(2,1000))