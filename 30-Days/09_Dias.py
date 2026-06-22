"""
1 - Serão duas entradas uma com o números de notas e as notas que formara uma lista
2 - A Saida será o resultado do calculo da média
3 - Ela deve receber uma lista de notas e retornar a média das notas
4 - Ele deve receber a informação de quantas notas serão passada
    Receber as notas e amazená-las em uma lista
    Chamar a função de calcular a média e exibir o resultado
5 - Usarei um laço de repetição para receber as notas e amazená-las em uma lista
    E depois passa essa lista para função onde usarei outro laço de repetição
    para percorre cada nota fazer a soma e dividir pelo o tamanho da lista e depois
    retornar o resultado
"""

quantidade_de_notas = int(input("Quantidade de notas: "))
notas = []


def calcular_media(lista_notas):
    somatoria_nota = 0
    for nota in lista_notas:
        somatoria_nota += nota
    return f"Média {somatoria_nota / len(lista_notas)}"


for i in range(1, quantidade_de_notas + 1):
    nota = float(input(""))
    notas.append(nota)

print(calcular_media(notas))
