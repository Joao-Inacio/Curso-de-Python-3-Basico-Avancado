"""
Fatiamento de strings
    012345678
    Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[2:5])
print(variavel[2:])
print(variavel[:5])
print(variavel[2:5:2])
print(variavel[::2])
print(variavel[len(variavel)])