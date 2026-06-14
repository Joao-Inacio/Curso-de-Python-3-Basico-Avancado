"""
1 - Será duas notas
2 - Será retornado o calculo da média
3 - Receber as duas notas fazer o calculo da média e retornar a mesma
4 - A chamada da função e talvez o print para exibir o resultado
5 - Acredito que será possível fazer tudo na linha do return
"""
def calcular_media(n1, n2):
    return (n1 + n2) / 2

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
print(f"Média: {calcular_media(n1=nota1, n2=nota2)}")
