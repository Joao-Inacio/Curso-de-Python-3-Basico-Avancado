"""
1 - A quantidade de participantes serão cadastrados e depois as idades válidas que devem estar entre 0 e 120 anos
2 - Será exibido 3 variáveis, a quantidade de participantes aptos e não aptos junto com a quantidade de idades inválidas
3 - O sistema vai receber a primeira entrada com o valor de quantos idade de participantes o sistema vai receber
e depois receberá a idade de cada participante e o sistema fará uma condicional para verificar se as idade então dentro do intervalo (0 e 120 anos) e depois exibira a quantidade de Aptos não Aptos e idade invalida
4 - irei usar um for junto com um condicional e alguns contadores
5 - irei usar 3 contadores
"""
quantidade_participante = int(input("Quantidade de participantes: "))
aptos = 0
nao_aptos = 0
idades_invalidas = 0
for i in range(1, quantidade_participante + 1):
    idade = int(input())
    if idade >= 18 and idade <= 120:
        aptos += 1
    elif idade < 18 and idade >= 0:
        nao_aptos += 1
    else:
        idades_invalidas += 1

print(f"Aptos: {aptos}")
print(f"Não aptos: {nao_aptos }")
print(f"Idades inválidas: {idades_invalidas}")
