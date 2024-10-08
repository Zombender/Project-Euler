def split_string_by_n(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

#number_list = [number_str[i:i+1] for i in range(0,len(number_str), separation)]
# Ejemplo de uso
cadena = "abcdefghij"
n = 3
resultado = split_string_by_n(cadena, n)
print(resultado)