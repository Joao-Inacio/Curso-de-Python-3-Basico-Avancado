
tipo_cha = int(input())
respostas = input()
numeros = [int(x) for x in respostas.split()]
corretos = 0

for i in range(0, len(numeros)):
    if numeros[i] == tipo_cha:
        corretos += 1
print(corretos)
"""3
4 1 1 2 1"""
