"""
Escreva um programa que solicita ao usuário um número e exiba se esse número é
par ou ímpar.
"""

numero = input("Insira um número: ")
try:
    if int(numero) % 2 == 0:
        print(f'O número {numero} é Par')
    else:
        print(f'O número {numero} é ímpar')
except:
    print(
        f'O valor {numero} não é um número. Por favor, insira apenas números válidos')
