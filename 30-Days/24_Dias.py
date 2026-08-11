def maior_valor(lista):
    if len(lista) > 0:
        maior_valor = lista[0]
        for i in lista:
            if i > maior_valor:
                maior_valor = i
        return maior_valor
    else:
        return lista



lista_numero = [-5, -2, -10, -1]
print(maior_valor(lista_numero))
