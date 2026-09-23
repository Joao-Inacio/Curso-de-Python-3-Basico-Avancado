def controle_estoque(colecao):
    resultado = []
    for item in colecao:
        if item["estoque"] < 10:
            resultado.append(item)
    for item in resultado:
        item["precisa_repor"] = True
    return resultado


produtos = [
    {"id": 1, "nome": "Notebook", "estoque": 3, "preco": 3500},
    {"id": 2, "nome": "Mouse", "estoque": 15, "preco": 80},
    {"id": 3, "nome": "Teclado", "estoque": 7, "preco": 150},
    {"id": 4, "nome": "Monitor", "estoque": 2, "preco": 1200},
    {"id": 5, "nome": "Cadeira", "estoque": 20, "preco": 900},
]

print(controle_estoque(produtos))
