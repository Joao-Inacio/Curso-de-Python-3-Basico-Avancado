"""
1 - Serão N entradas, cada entrada com uma nota por participante
2 - A Saida será a soma de todas as notas de entradas
3 - 1º Será informando a quantidade de notas que o sistema receberá
    2° Será recebido as nota de cada participante
    3° Será feita a soma de todas as notas
    4° Será exibido o resultado da soma
4 - Pretendo usar um laço for para iterar no intervalo N+1 e é possível guardar em uma lista ou um dicionario
Mais usarei o dicionario pois vai ficar mais organizado e será possível consulta as notas individual dos participante
"""
entradas = int(input("Quantidade de participantes: "))
notas = []
soma = 0
for i in range(1, entradas + 1):
    nota = int(input(f"Participante {i}: "))
    notas.append(nota)

for i in notas:
    soma += i

print(f"Pontuação total: {soma}")

