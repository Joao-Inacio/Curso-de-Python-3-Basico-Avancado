def resumo_cliente(colecao_clientes, colecao_pedido):
    resumo = {}
    for cliente in colecao_clientes:
        id_cliente = cliente["id"]
        if id_cliente not in resumo:
            resumo[id_cliente] = {"quantidade_pedidos": 0, "valor_total": 0}
        for pedido in colecao_pedido:
            if id_cliente == pedido["cliente_id"]:
                resumo[id_cliente]["quantidade_pedidos"] += 1
                resumo[id_cliente]["valor_total"] += pedido["valor"]
    return resumo


clientes = [
    {"id": 1, "nome": "João", "cidade": "Fortaleza"},
    {"id": 2, "nome": "Maria", "cidade": "Recife"},
    {"id": 3, "nome": "Carlos", "cidade": "São Paulo"},
]

pedidos = [
    {"id": 101, "cliente_id": 1, "valor": 150},
    {"id": 102, "cliente_id": 2, "valor": 300},
    {"id": 103, "cliente_id": 1, "valor": 200},
    {"id": 104, "cliente_id": 3, "valor": 500},
    {"id": 105, "cliente_id": 2, "valor": 100},
]

print(resumo_cliente(clientes, pedidos))
