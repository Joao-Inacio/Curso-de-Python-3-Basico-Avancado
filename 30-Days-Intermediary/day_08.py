def valor_total(colecao, categoria):
    valor_final = 0
    for item in colecao:
        if item["categoria"] == categoria:
            valor_final += item["valor"]
    return valor_final


vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 3500},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 80},
    {"produto": "Cadeira", "categoria": "Móveis", "valor": 700},
    {"produto": "Teclado", "categoria": "Eletrônicos", "valor": 150},
    {"produto": "Mesa", "categoria": "Móveis", "valor": 900},
]
teste = []
print(valor_total(teste, "Roupas"))
