def resumo_vendas(colecao):
    resumo = {}
    for item in colecao:
        if item["status"] == "aprovada":
            categoria = item["categoria"]
            if categoria not in resumo:
                resumo[categoria] = {"quantidade": 0, "valor_total": 0}
            resumo[categoria]["quantidade"] += 1
            resumo[categoria]["valor_total"] += item["valor"]

    return resumo


vendas = [
    {
        "produto": "Notebook",
        "categoria": "Eletrônicos",
        "valor": 3500,
        "status": "aprovada",
    },
    {
        "produto": "Mouse",
        "categoria": "Eletrônicos",
        "valor": 80,
        "status": "cancelada",
    },
    {"produto": "Cadeira", "categoria": "Móveis", "valor": 700, "status": "aprovada"},
    {
        "produto": "Teclado",
        "categoria": "Eletrônicos",
        "valor": 150,
        "status": "aprovada",
    },
    {"produto": "Mesa", "categoria": "Móveis", "valor": 900, "status": "cancelada"},
    {
        "produto": "Monitor",
        "categoria": "Eletrônicos",
        "valor": 1200,
        "status": "aprovada",
    },
]

print(resumo_vendas(vendas))
