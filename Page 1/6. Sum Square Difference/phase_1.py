def sum_square_numbers(limit: int):
    result = 0
    for x in range(1,limit+1):
        result += x**2
    return result
def square_sum_numbers(limit: int):
    sum_result = (limit*(limit+1))//2
    return sum_result**2

sum = sum_square_numbers(100)
square = square_sum_numbers(100)

print(f'{square} - {sum} = {square-sum}')