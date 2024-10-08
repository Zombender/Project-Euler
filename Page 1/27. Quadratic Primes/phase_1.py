def quadratic_formula_80(n):
    return n**2 - 79*n + 1601

def quadratic_formula_40(n):
    return n**2 +n +41

def quadratic_formula_x(n):
    return n**2 + n +1

for i in range(40):
    print(f'{i}: {quadratic_formula_x(i)}')