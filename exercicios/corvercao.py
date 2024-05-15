"""
Crie um programa que converta graus Celsius para Fahrenheit. 
A fórmula de conversão é: Fahrenheit = (Celsius × 9/5) + 32.
"""

graus = input("Digite a temperatura em graus Celsius: ")

try:
    fahr = (float(graus) * 9 / 5) + 32
    print(f'{graus}° em graus Celsius é igual a {fahr}° em Fahrenheit')
except:
    print(f'{graus} não é um valor valido, insira um valor valido')