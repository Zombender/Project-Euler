
def set_distinct_powers(min,max)->set:
    set_distinct_powers = set()
    for a in range(min,max):
        for b in range(min,max):
            set_distinct_powers.add(a**b)
    return len(set_distinct_powers)


print(set_distinct_powers(2,100))