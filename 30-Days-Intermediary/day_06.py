def resumo_vendas(colecao):
    resumo = {}
    for item in colecao:
        categoria = item["categoria"]
        valor = item["valor"]
        if categoria not in resumo:
            resumo[categoria] = {
                "quantidade": 0,
                "valor_total": 0,
            }
        resumo[categoria]["quantidade"] += 1
        resumo[categoria]["valor_total"] += valor
    return resumo


vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 3500},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 80},
    {"produto": "Cadeira", "categoria": "Móveis", "valor": 700},
    {"produto": "Teclado", "categoria": "Eletrônicos", "valor": 150},
    {"produto": "Mesa", "categoria": "Móveis", "valor": 900},
]
print(resumo_vendas(vendas))
