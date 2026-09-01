def atualizar_estoque(colecao, id, quantidade):
    for item in colecao:
        if item['id'] == id:
            novo_estoque = item['estoque'] + quantidade
            if novo_estoque <= item['estoque_maximo']:
                item['estoque'] = novo_estoque
    return colecao



produtos = [
    {
        "id": 1,
        "nome": "Notebook",
        "estoque": 5,
        "estoque_maximo": 10
    },
    {
        "id": 2,
        "nome": "Mouse",
        "estoque": 8,
        "estoque_maximo": 10
    },
    {
        "id": 3,
        "nome": "Teclado",
        "estoque": 3,
        "estoque_maximo": 5
    }
]
print(atualizar_estoque(produtos, 1, 0))
