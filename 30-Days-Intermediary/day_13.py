def encontrar_indices_estoque_baixo(produtos):
    indices = []
    for ids, item in enumerate(produtos, start=1):
        if item["estoque"] < 10:
            indices.append(ids)
    return indices


produtos = [
    {"nome": "Notebook", "estoque": 10},
    {"nome": "Mouse", "estoque": 10},
    {"nome": "Teclado", "estoque": 7},
    {"nome": "Monitor", "estoque": 2},
]

print(encontrar_indices_estoque_baixo(produtos))
