def resumir_por_cidade(pedidos):
    resumo = {}
    for item in pedidos:
        cidade = item['cidade']
        if cidade not in resumo:
            resumo[cidade] = {'quantidade': 0, 'valor_total': 0}

        resumo[cidade]['quantidade'] += 1
        resumo[cidade]['valor_total'] += item['valor']

    return resumo

pedidos = [
    {"id": 1, "cliente": "Ana", "cidade": "Fortaleza", "valor": 150.0},
    {"id": 2, "cliente": "Carlos", "cidade": "Recife", "valor": 200.0},
    {"id": 3, "cliente": "João", "cidade": "Fortaleza", "valor": 100},
]

print(resumir_por_cidade(pedidos))
