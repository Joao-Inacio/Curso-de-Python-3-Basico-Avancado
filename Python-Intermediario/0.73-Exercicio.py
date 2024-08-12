# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplicar(2, 3, 4, 5, 6, 7, 8, 9, 10)
print(resultado)

def par_impar(numero):
    if numero % 2 == 0:
        return "Número é Par"
    return "Número é Ímpar"


print(par_impar(2))
print(par_impar(3))