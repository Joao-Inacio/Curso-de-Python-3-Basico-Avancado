"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Dobrar o número: ')


try:
    numero = float(numero)
    print(f'O dobro de {numero} é {numero * 2:.2f}')
except:
    print('Você não digitou um número')
