"""
Lista de listas e seus índices
"""

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0       1       2       3
    ['Elton', 'Rafael', 'Bia', 'Vinícius', ],  # 1
]
print(salas[1][2])  # Bia
print(salas[0][0])  # Maria

for sala in salas:
    for aluno in sala:
        print(aluno)

