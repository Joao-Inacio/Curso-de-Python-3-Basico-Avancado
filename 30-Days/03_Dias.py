"""
1 - A primeira entrada será a quantidade de participante e depois notas para cada participante
2 - A Saida sera a soma da quantidade de participante qua atingiram maior ou igual 70
que será clarificado como aprovado e os participante que não atingiram será clarificado reprovados
3 - O Sistema irá receber um número que representa a quantidade de participante
e depois pedira as nota de cada participante onde será aplicada um condição para clarificar com aprovado e reprovado
e por fir exibirá a quantidade de cada grupo
4 - Irei utilizar um laço de repetição for com um condicional if e uma variável acumuladora
"""
quantidades = int(input("Quantidade de participante: "))
aprovados = 0
reprovados = 0
for i in range(1, quantidades + 1):
    nota = int(input(f"Nota participante {i}: "))
    if nota >= 70:
        aprovados += 1
    else:
        reprovados += 1
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
