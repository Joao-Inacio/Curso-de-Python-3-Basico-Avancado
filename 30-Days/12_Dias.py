"""
1 - A quantidade de notas e depois todas as notas e por fim a nota minima
2 - A lista original com todas as nota e a segunda lista contendo a lista das notas dos aprovados
3 - Vai receber a lista de notas e a nota minima e retornar uma nova lista das notas dos aprovados
4 - Sera responsável por receber a quantidade de nota e a lista de nota e repassar para a função
e por fim exibir a lista original e a lista das notas dos aprovados
5 - vou usar um laço for para inteira as nota e armazena-las em uma lista e passar para a função
e dentro da função vou usar um if para adicionar as notas aprovadas dentro de outa lista e retornar essa lista
"""


def filtrar_aprovados(lista_notas, nota_minima):
    lista_aprovados = []
    for nota in lista_notas:
        if nota >= nota_minima:
            lista_aprovados.append(nota)
    return lista_aprovados


quantidade_notas = int(input("Quantidade de notas: "))
lista_nota_original = []
for i in range(0, quantidade_notas):
    nota = float(input())
    lista_nota_original.append(nota)

nota_minima = float(input("Nota minima: "))
print(f"Lista original: {lista_nota_original}")
print(f"Aprovados: {filtrar_aprovados(lista_nota_original, nota_minima)}")
