"""
1️⃣ Exercício: Dobrar Números
Crie uma função lambda que recebe um número e retorna o dobro dele.
Teste a função com pelo menos três números diferentes.
"""
dobro = lambda x: x * 2
print(dobro(4))

"""
xercício: Filtrar Números Pares
Dada uma lista de números, use filter() e uma função lambda para manter apenas
os números pares
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x%2 == 0, numeros))
print(pares)

"""
3️⃣ Exercício: Ordenar uma Lista de Tuplas
Dada uma lista de tuplas representando pessoas ((nome, idade)), use sorted()
com uma função lambda para ordenar a lista pela idade.
"""
pessoas = [('Ana', 25), ('Carlos', 40), ('Bruno', 30)]
ordenado = sorted(pessoas, key=lambda x: x[1])
print(ordenado)  # Deve imprimir [('Ana', 25), ('Bruno', 30), ('Carlos', 40)]

