def encontrar_ids_duplicados(colecao):
    valores = [d["id"] for d in colecao]
    ids = []
    for i, elemento in enumerate(valores):
        if elemento in valores[i + 1 :]:
            ids.append(elemento)
    return set(ids)


registros = [
    {"id": 101, "nome": "Ana"},
    {"id": 101, "nome": "Carlos"},
    {"id": 101, "nome": "João"},
    {"id": 103, "nome": "Maria"},
    {"id": 103, "nome": "Pedro"},
]

print(encontrar_ids_duplicados(registros))
