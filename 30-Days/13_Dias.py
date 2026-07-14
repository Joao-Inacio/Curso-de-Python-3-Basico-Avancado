"""
1- Serão 3 entradas sendo elas a quantidade de notas depois todas as notas e por fim a nota minima
2- Serão 2 saídas sendo elas a lista dos aprovados e a média dos aprovados
3- A primeira função 'filtrar_aprovados' deve receber uma lista de notas e uma nota minima e retornar uma nova lista
contendo apenas as notas aprovadas já a segunda função 'calcular_media' deve receber a lista de notas vinda da primeira
função e retornar a média das notas e caso a lista esteja vazia, a função deve retornar 0.
4- Ficará responsável por receber a quantidade de notas e depois todas as notas e receber a nota minima e por fim exibir
a lista dos aprovados e a média dos aprovados.
5- Usarei um laço for e if principalmente dentro da primeira função e para receber as notas
"""


def filtrar_aprovados(lista_notas, nota_minima):
    aprovados = []
    for nota in lista_notas:
        if nota >= nota_minima:
            aprovados.append(nota)
    return aprovados


def calcular_media(lista_nota):
    media = 0
    if len(lista_nota) > 0:
        for nota in lista_nota:
            media += nota
        return media / len(lista_nota)
    else:
        return 0


quantidade_notas = int(input("Quantidade de notas: "))
lista_nota_original = []
for _ in range(0, quantidade_notas):
    nota = float(input())
    lista_nota_original.append(nota)

nota_minima = float(input("Nota minima: "))

print(f"Aprovados: {filtrar_aprovados(lista_nota_original, nota_minima)}")
print(
    f"Média dos aprovados: {calcular_media(filtrar_aprovados(lista_nota_original, nota_minima))}"
)
