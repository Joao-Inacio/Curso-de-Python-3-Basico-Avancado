# Manipulando chaves e valores em dicionários


pessoa = {}
chave = 'sobrenome'
pessoa['nome'] = 'João'
pessoa[chave] = 'Inácio'
print(pessoa)
del pessoa[chave]
print(pessoa)

if pessoa.get(chave) is None:
    print('Não exite')
