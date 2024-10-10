def fifth_power_number(number:int)->bool:
    total = 0
    for digit in str(number):
        total += int(digit)**5
    return True if total == number else False

fifth_power_numbers_list = [n for n in range(2,1000000) if fifth_power_number(n)]

print(sum(fifth_power_numbers_list))