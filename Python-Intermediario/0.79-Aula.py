# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
from copy import deepcopy


pessoa = {
    'nome': 'João',
    'sobrenome': 'Inácio',
}
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

pessoa.setdefault('idade', 0)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}

d2 = deepcopy(d1)

d2['c1'] = 100
d2['l1'][1] = 10

print(d1)
print(d2)

print(pessoa.get('nome'))

nome = pessoa.pop('nome')
print(nome)
pessoa.update({
    'nome': 'Igna',
})

