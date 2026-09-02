def atualizar_cidade(colecao, id, cidade):
    for item in colecao:
        if item["id"] == id:
            item["fornecedor"]["cidade"] = cidade
    return colecao


produtos = [
    {
        "id": 1,
        "nome": "Notebook",
        "categoria": "Eletrônicos",
        "fornecedor": {"nome": "Tech Distribuidora", "cidade": "São Paulo"},
    },
    {
        "id": 2,
        "nome": "Mouse",
        "categoria": "Eletrônicos",
        "fornecedor": {"nome": "InfoTech", "cidade": "Recife"},
    },
    {
        "id": 3,
        "nome": "Cadeira",
        "categoria": "Móveis",
        "fornecedor": {"nome": "Móveis Brasil", "cidade": "Fortaleza"},
    },
]
print(atualizar_cidade(produtos, 1, "SP"))
