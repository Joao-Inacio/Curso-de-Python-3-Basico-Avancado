def clientes_alto_valor(colecao):
    alto_valor = []
    for i, elementos in enumerate(colecao):
        if elementos["compras"] >= 5 and elementos["valor_total"] >= 700:
            alto_valor.append(elementos)
    return alto_valor


clientes = [
    {"nome": "Ana", "idade": 25, "compras": 5, "valor_total": 750.0},
    {"nome": "Carlos", "idade": 31, "compras": 2, "valor_total": 200.0},
    {"nome": "João", "idade": 42, "compras": 8, "valor_total": 1200.0},
    {"nome": "Maria", "idade": 19, "compras": 1, "valor_total": 50.0},
    {"nome": "Pedro", "idade": 35, "compras": 6, "valor_total": 900.0},
]

print(clientes_alto_valor(clientes))
