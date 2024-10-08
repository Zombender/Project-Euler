#File lost, I will do it in the future

def define_range(number: int):
    range_q = 1
    for i in range(number):
        range_q *=10
    return range_q+1

def digits(number:int):
    return len(str(number))

def palindrome(number:int):
    number_str = str(number)
    len_number = int(len(number_str)/2)
    left = number_str[:len_number]
    right = number_str[len_number:]
    if left == right[::-1]:
        return True
    return False

def palindrome_number(digit_q):
    largest_palindrome = 0
    for i in range(digit_q):
        for j in range(digit_q):
            number = i*j
            if int(digits(number)) % 2 !=0:
                continue
            elif palindrome(number):
                if largest_palindrome < number:
                    largest_palindrome = number
    return largest_palindrome

print(palindrome_number(define_range(3)))
