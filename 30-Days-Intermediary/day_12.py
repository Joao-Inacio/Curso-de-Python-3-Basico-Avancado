def atualizar_produto(produtos, id, novo_preco):
    novos_produtos = []
    for item in produtos:
        novo_item = item.copy()
        if novo_item["id"] == id:
            novo_item["preco"] = novo_preco
        novos_produtos.append(novo_item)
    return novos_produtos


produtos = [
    {"id": 1, "nome": "Notebook", "estoque": 3, "preco": 3500},
    {"id": 2, "nome": "Mouse", "estoque": 15, "preco": 80},
    {"id": 3, "nome": "Teclado", "estoque": 7, "preco": 150},
]

print(atualizar_produto(produtos, 2, 1000))
print(produtos)
