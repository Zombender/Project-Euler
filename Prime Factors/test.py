def is_prime(n):

    status = True
    for i in range(2,int(n**0.5)+1): 
       if n % i == 0 :
            status = False 
            break
    return status
y=[]
for i in range (600851475143 , 1 , -1): 
        if is_prime(i):
            if 600851475143%i == 0:
                 y.append(i)
                 break
        
print(y)