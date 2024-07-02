"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('joão')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

for item in enumerate(lista):
    print(item)

nova_lista = list(enumerate(lista))
print(nova_lista)

for indice, nome in enumerate(lista):
    print(indice)
    print(nome)
