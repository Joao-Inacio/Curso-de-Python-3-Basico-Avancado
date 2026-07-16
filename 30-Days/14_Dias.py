"""
1- A quantidade de notas e as notas
2- A saída será a Maior nota, Menor nota e Média
3- Ela deve receber uma lista de notas  E retornar a maior nota, menor nota e a
média da turma.
4- Deve perguntar quantas notas serão informadas e receber todas as notas depois
armazená-las em uma lista, chamar a função e por fim Exibir a maior nota, menor nota e a
média da turma.
5-
Receber os dados

↓

Criar a lista de notas

↓

Gerar as estatísticas

↓

Exibir os resultados
"""


def gerar_estatisticas(lista_notas):
    maior_nota = lista_notas[0]
    menor_nota = lista_notas[0]
    media = 0
    for nota in lista_notas:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        media += nota
    return maior_nota, menor_nota, (media / len(lista_notas))


quantidade_notas = int(input("Quantidade de notas: "))
lista_nota_original = []
for _ in range(0, quantidade_notas):
    nota = float(input())
    lista_nota_original.append(nota)


maior_nota, menor_nota, media = gerar_estatisticas(lista_nota_original)
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média: {media}")
