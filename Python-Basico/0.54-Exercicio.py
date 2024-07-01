"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
indice = 0

lista.append('João')
for nome in lista:
    print(indice, nome)
    indice += 1
