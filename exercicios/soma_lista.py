"""
Soma de Números em uma Lista:
Crie um programa que solicite ao usuário uma lista de números e calcule a soma
de todos os números da lista.
"""

lista = []
try:
    while True:
        numero = float(input("Digite um Número: "))
        lista.append(numero)
        if len(lista) > 3:
            continua = str(input("Deseja continuar [S]Sim ou [N]Não: "))
            if continua.upper() == 'N':
                break
    novo = 0
    soma = 0
    for i in lista:
        novo = i
        soma = soma + novo
    print(soma)
except:
    print('Você não digitou um número valido, digite um número valido')
