
def lexicographic_permutation(elements : list):
    if len(elements) == 1:
        return [elements]
    result = []
    for i in range(len(elements)):
        element = elements[i]
        left = elements[:i] + elements[i+1:]
        for permutation in lexicographic_permutation(left):
            result.append([element] + permutation)
    return sorted(result,key=lambda x: int(''.join(number for number in x)))
    

numbers = ['0','1','2','3','4','5','6','7','8','9']
permutations = lexicographic_permutation(numbers)
print(permutations[1000000-1])
