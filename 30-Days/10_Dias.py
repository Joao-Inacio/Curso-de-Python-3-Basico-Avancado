"""
1 - A quantidade de notas, as notas que serão armazenadas em uma lista e a nota minima
2 - A quantidades de aprovados
3 - Receber um lista de notas e um nota minima e ratonara quantos foram aprovados
4 - Ficara responsável por receber a quantidade de notas e as notas que serão armazenadas em uma lista
e a exibição do resultado
5 - Vou utilizar um for para iterar no intervalo das quantidades de notas e receber cada nota onde ser
serão armazenadas em uma lista
"""


def contar_aprovados(lista_nota, nota_minima):
    aprovados = 0
    for nota in lista_nota:
        if nota >= nota_minima:
            aprovados += 1
    return aprovados


quantidade_notas = int(input("Quantidade de notas: "))
notas = []
for i in range(1, quantidade_notas + 1):
    nota = float(input())
    notas.append(nota)

nota_minima = float(input("Nota mínima: "))

print(contar_aprovados(notas, nota_minima))
