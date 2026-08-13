def contagem_ocorrencia(lista, numero_especifico):
    contagem = 0
    for i in lista:
        if i == numero_especifico:
            contagem += 1
    return contagem


lista_numeros = []
nomero_procurado = 3

print(f"Resultado: {contagem_ocorrencia(lista_numeros, nomero_procurado)}")
