class MathHelper():
    
    @staticmethod
    def is_prime(number:int)->bool:
        if number < 0: number*=-1
        if number == 1:return False
        elif number  < 4: return True
        elif number %2 == 0: return False
        elif number < 9 : return True
        elif number %3 == 0: return False
        sqr = round(number**0.5)
        f= 5
        while f <= sqr:
            if number % f == 0: return False
            if number % (f+2) == 0: return False
            f+=6
        return True
    
    @staticmethod
    def prod(array:list|tuple):
        result = 1
        for i in array:
            result *=i
        return result
    
    @staticmethod
    def gcd(a: int,b: int)->int: 
        if a == 0:
            return b
        return MathHelper.gcd(b%a,a)

    @staticmethod
    def lcd(a: int, b:int) ->int:
        return a*b // MathHelper.gcd(a,b)
    
    @staticmethod
    def factorial(number: int) ->int:
        result = 1
        for num in range(1, number+1):
            result *=num
        return result

    @staticmethod
    def d(number:int) ->set:
        max_factor = int(number **0.5)
        factors = []
        for i in range(1,max_factor+1):
            if number %i == 0:
                factors.append(i)
                factors.append(int(number/i))
        return set(filter(lambda x : x<=number//2,factors))
    
    @staticmethod
    def palindrome(number:str):
        len_number = len(number)
        left = number[:len_number//2]
        if len_number %2 == 0:
            right = number[len_number//2:]
        else:
            right = number[len_number//2+1:]
        return left == right[::-1]
    
    def is_pandigital(number:str):
        one_to_nine:str = ''.join([str(num) for num in range(1,10)])
        number = ''.join(sorted(number))
        if one_to_nine == number:
            return True
        return False


if __name__ == '__main__':
    is_pandigital = MathHelper.is_pandigital('918273645')
    print(is_pandigital)
