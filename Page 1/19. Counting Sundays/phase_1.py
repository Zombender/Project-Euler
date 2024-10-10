months = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6: 30,
    7: 31,
    8: 31, 
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}

def leap_year(year):
    return True if (year %400 == 0) else False if (year %100==0) else True if (year %4 == 0) else False

def sum_starting_point(starting_point, month):
    match month:
        case 31:
            return starting_point +3
        case 30:
            return starting_point +2
        case 29:
            return starting_point +1
        case 28:
            return starting_point
    return starting_point
        
def calculate_sundays():
    total_sundays = 0
    starting_point = 2
    for year in range(1901, 2001):
        this_year_months = months
        if leap_year(year): this_year_months[2]+=1
        for month in range(1,13):
            if starting_point > 7:starting_point -=7
            if starting_point == 1:
                total_sundays +=1
            starting_point = sum_starting_point(starting_point,this_year_months[month])
    return total_sundays

print(calculate_sundays())
            
            