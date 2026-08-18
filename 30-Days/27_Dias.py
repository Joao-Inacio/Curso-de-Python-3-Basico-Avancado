def maior_valor(colecao, variavel):
    valores = [d[variavel] for d in colecao]
    maior_valor = valores[0]
    for i in range(len(valores)):
        if valores[i] > maior_valor:
            maior_valor = valores[i]
    return maior_valor

registros = [
    {"idade": 25, "score": 0.72},
    {"idade": 31, "score": 0.85},
    {"idade": 19, "score": 0.64},
    {"idade": 42, "score": 0.91},
]
print(maior_valor(registros, 'idade'))
