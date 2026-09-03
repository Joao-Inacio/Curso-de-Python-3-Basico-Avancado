def atualizar_estoque(colecao, id, quantidade):
    for item in colecao:
        if item['id'] == id:
            if item['estoque'] < 10:
                item['estoque'] += quantidade
    return colecao

produtos = [
    {
        "id": 1,
        "nome": "Notebook",
        "categoria": "Eletrônicos",
        "estoque": 5,
        "preco": 3500
    },
    {
        "id": 2,
        "nome": "Mouse",
        "categoria": "Eletrônicos",
        "estoque": 15,
        "preco": 80
    },
    {
        "id": 3,
        "nome": "Cadeira",
        "categoria": "Móveis",
        "estoque": 3,
        "preco": 700
    }
]
print(atualizar_estoque(produtos, 1, 20))
