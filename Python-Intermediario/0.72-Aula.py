"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(soma_1_2_3)
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros)
print(outra_soma)
