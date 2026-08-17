def valor_duplicado(lista):
    return len(lista) != len(set(lista))

lista = [7]
print(valor_duplicado(lista))
