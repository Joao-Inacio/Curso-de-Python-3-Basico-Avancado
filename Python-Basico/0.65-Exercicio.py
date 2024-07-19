"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

numero = str(input("Digite um número de CPF: ")).replace('.', '').replace('-', '')

try:
    cpf = [int(i) for i in numero]
    nove_digito = cpf[:9]
    n = 0
    lista = []
    soma = 0
    for i in range(10, 1, -1):
            lista.append(i * nove_digito[n])
            n += 1
    for i in lista:
        soma += i
    if soma * 10 % 11 > 9:
        print('Digito = 0')
    else:
        print(f'0 Primeiro Digito é {soma * 10 % 11}')
except:
    print("Apenas números são permitidos!")



"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
ultimo_digito = cpf[:10]
nova_lista = []
n = 0
nova_soma = 0
for i in range(11, 1, -1):
    nova_lista.append(i * ultimo_digito[n])
    n += 1
for i in nova_lista:
    nova_soma += i
if nova_soma * 10 % 11 > 9:
    print('Digito = 0')
else:
    print(f'0 Segundo  Digito é {nova_soma * 10 % 11}')


