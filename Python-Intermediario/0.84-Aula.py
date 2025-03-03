#  Funções lambda complexas (para entendimento)

def executa(funcao, *args):
    return funcao(*args)


print(executa(lambda x, y: x + y, 2, 3))

