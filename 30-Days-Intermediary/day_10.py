def segundo_maior_valor(lista):
    if len(lista) < 2:
        return None

    maior = lista[0]
    segundo_maior = None

    for i in lista:
        if i > maior:
            segundo_maior = maior
            maior = i
        elif i < maior:
            if segundo_maior is None or i > segundo_maior:
                segundo_maior = i

    return segundo_maior


vendas = [3500, 80, 700, 150, 900, 1200, 1500]

print(segundo_maior_valor(vendas))
