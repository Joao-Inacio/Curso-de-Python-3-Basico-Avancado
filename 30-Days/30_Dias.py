def avaliar_desempenho(colecao):
    bom_desempenho = []
    for elementos in colecao:
        if elementos["horas_estudo"] >= 8 and elementos["nota_prova"] >= 7:
            bom_desempenho.append(elementos)
    return bom_desempenho


alunos = [
    {"nome": "Ana", "horas_estudo": 10, "nota_prova": 8.5},
    {"nome": "Carlos", "horas_estudo": 3, "nota_prova": 5.0},
    {"nome": "João", "horas_estudo": 15, "nota_prova": 9.0},
    {"nome": "Maria", "horas_estudo": 6, "nota_prova": 6.5},
    {"nome": "Pedro", "horas_estudo": 12, "nota_prova": 7.5},
]

print(avaliar_desempenho(alunos))
