"""
1 - Recebe a quantidade de notas e depois recebe cada nota
2 - A Saida será a informação se a nota for inválida e a quantidade de notas válidas
3 - Será responsável por receber uma nota e retornar True se a nota estiver entre 0 e 10 ou False caso contrário
4 - Receber a quantidade de notas e as notas depois armazená-la em uma lista se for válida caso contrario informa que a nota é invalida e ao final exibir o total de notas validas armazenadas
5 - Pretendo usar um laço for para inteira a quantidade de notas e depois o if usando a função para armazenar as notas validas e no else exibir se a nota for invalida e por fim um print com o len da lista
"""


def validar_nota(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False


quantidade_notas = int(input("Quantidade de notas: "))
notas_validas = []
for i in range(1, quantidade_notas + 1):
    nota = float(input())
    if validar_nota(nota):
        notas_validas.append(nota)
    else:
        print("Nota inválida!")

print(len(notas_validas))
