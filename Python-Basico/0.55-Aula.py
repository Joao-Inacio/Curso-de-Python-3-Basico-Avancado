"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes


nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

print(nome1)

nome1, *_ = ['Maria', 'Helena', 'Luiz']

print(nome1)
print(_)

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)


