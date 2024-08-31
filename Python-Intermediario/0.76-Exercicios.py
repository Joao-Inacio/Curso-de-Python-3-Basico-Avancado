# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def receber_numero(numero):
    def multiplicar(multiplicador):
        return numero * multiplicador
    return multiplicar


duplicar = receber_numero(2)
triplicar = receber_numero(3)

print(duplicar(2))
print(triplicar(2))
    