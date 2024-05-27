def palindrome(n):
    largest = 0 
    x = n
    y = n 

    for i in range(x, 0, -1): 
        for j in range(y, 0, -1): 
            test = str(i * j) 
            if test == test[::-1]: 
                largest = max(largest, i * j)

    return largest  
    
def main():
    number = 999
    print(palindrome(number))

if __name__ == "__main__":
    main()  
 