"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(x, y, z, x + y + z)
    else:
        print(x + y)
# Valores padrão para parâmetros em funções Python + NoneType e None


soma(2, 3)  # 5
soma(4, 5)  # 9
soma(1, 2, 3)  # 6
