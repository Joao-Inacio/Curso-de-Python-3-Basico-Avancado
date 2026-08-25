def processar_clientes(colecao):
    nova_colecao = {}
    somatorio_valor = 0.0
    for elementos in colecao:
        ids = elementos["id"]
        for valor_str in elementos["compras"]:
            try:
                valor_float = float(valor_str)
                somatorio_valor += valor_float
            except:
                continue
        nova_colecao[ids] = {
            "id": elementos["id"],
            "nome": elementos["nome"],
            "quantidade_compras": len(elementos["compras"]),
            "valor_total": somatorio_valor,
        }
        somatorio_valor = 0.0
    return nova_colecao


clientes = [
    {"id": 1, "nome": "Ana", "compras": ["120.50", "80.00", "50.00"]},
    {"id": 2, "nome": "Carlos", "compras": ["300.00", "150.00"]},
    {"id": 3, "nome": "João", "compras": []},
]

print(processar_clientes(clientes))
