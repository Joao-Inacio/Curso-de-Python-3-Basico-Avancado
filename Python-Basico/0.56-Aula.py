"""
Tipo tupla - Uma lista imutável
"""

nomes = 'Maria', 'Helena', 'Luiz'
print(nomes, type(nomes))

nomes = ('Maria', 'Helena', 'Luiz')
print(nomes, type(nomes))

nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
print(nomes, type(nomes))
