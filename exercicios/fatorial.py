"""
Fatorial de um Número:

Escreva um programa que solicite um número ao usuário e calcule seu fatorial.
"""
try:
    numero = int(input("Digite um número: "))
    novo = 0
    soma = 1
    for i in range(1, numero + 1):
        novo = i
        soma = soma * novo
    print(f'O Fatorial de {numero}! = {soma}')

except:
    print("Você digitou um número invalido, digite um número valido")