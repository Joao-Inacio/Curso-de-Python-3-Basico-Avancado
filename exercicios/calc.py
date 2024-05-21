"""
Calculadora Simples:
Escreva um programa que solicite dois números e uma operação 
(soma, subtração, multiplicação ou divisão) e exiba o resultado da operação.
"""

try:
    numero1 = int(input("Digite um Número: "))
    numero2 = int(input("Digite o segundo Número: "))
    operacao = str(input("""
            Qual operação?
            [+] Soma
            [-] Subtração
            [*] Multiplicação
            [/] Divisão
    """)
    )
    if operacao == '+':
        print(f'A soma de {numero1} + {numero2} = {numero1 + numero2}')
    if operacao == '-':
        print(f'A subtração de {numero1} - {numero2} = {numero1 - numero2}')
    if operacao == '*':
        print(f'A multiplicação de {numero1} * {numero2} = {numero1 * numero2}')
    if operacao == '/':
        print(f'A divisão de {numero1} / {numero2} = {numero1 / numero2}')

except:
    print("Você digitou um número invalido, digite um número valido")
