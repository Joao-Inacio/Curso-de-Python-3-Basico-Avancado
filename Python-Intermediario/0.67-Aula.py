"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y,z):
    print(f'{x=} y={y} {z=}')


soma(y=1, x=3, z=3)
soma(5, 3, 3)
