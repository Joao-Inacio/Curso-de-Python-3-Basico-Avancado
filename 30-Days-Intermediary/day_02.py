def atualizar__estoque(colecao, id, quantidade):
    for item in colecao:
        if item['id' ] == id:
            item['estoque'] += quantidade
    return colecao


produtos = [
    {"id": 1, "nome": "Notebook", "categoria": "Eletrônicos", "estoque": 5},
    {"id": 2, "nome": "Mouse", "categoria": "Eletrônicos", "estoque": 12},
    {"id": 3, "nome": "Cadeira", "categoria": "Móveis", "estoque": 3},
]


print(atualizar__estoque(produtos, 8, 10))
