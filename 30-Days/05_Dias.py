"""
1 - A Entrada será uma nome(string)
2 - A Saida será exibido uma mensagem dizendo quantas letras 'a' foram encontradas no nome
3 - O sistema recebe um nome e fará a conta de quantas letras a tem e exibirá a quantidade
4 - Vou tenta usar o for para percorrer a string e farei uma comparação
5 - Acredito que sim para conta a quantidade de ocorrência
"""

nome = str(input()).lower()
letras_a = 0
for i in nome:
    if i == 'a':
        letras_a += 1

print(f"Quantidade de letras 'a': {letras_a}")

