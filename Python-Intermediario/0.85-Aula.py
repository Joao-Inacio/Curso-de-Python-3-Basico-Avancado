# Empacotamento e desempacotamento de dicionários


a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
a, b = pessoa.items()
print(a, b)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

def motra_argumentos_nomeados(*args, **kwargs):
    print(f'Não nomeados: {args}')
    for chave, valor in kwargs.items():
        print(chave, valor)

motra_argumentos_nomeados(1, 2, nome='João')
