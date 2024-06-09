one_nineteen_dict = {
    '00' : '',
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3': 'three',
    '4': 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
}

decil_hundred = {
    '2' : 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5' : 'fifty',
    '6' : 'sixty',
    '7' : 'seventy',
    '8' : 'eighty',
    '9' : 'ninety',
    'hundred' : 'hundred'
}
def digits(number:int):
    return len(str(number))

def convert_number_to_string(number: str, digits_ : int) ->int:
    match digits_:
        case 1:
            return len(one_nineteen_dict[number])
        case 2:
            total_digits = 0
            if int(number[0]) >=2:
                total_digits += len(decil_hundred[number[0]])
                return total_digits + len(one_nineteen_dict[number[1]])
            return len(one_nineteen_dict[number])
        case 3:
            total_digits = 0
            total_digits+= len(one_nineteen_dict[number[0]])+len(decil_hundred['hundred'])
            if int(number[1]) >=2:
                total_digits += len(decil_hundred[number[1]])
                return total_digits + len(one_nineteen_dict[number[2]])+3
            elif int(number[1]) == 1:
                return total_digits + len(one_nineteen_dict[number[1:]])+3
            elif int(number[2]) !=0:
                return total_digits + len(one_nineteen_dict[number[2]])+3
            else:
                return total_digits + len(one_nineteen_dict[number[2]])
        case 4:
            return 11
        
total = [convert_number_to_string(str(x),digits(x)) for x in range (1,1001)]
print(sum(total))

