"""
if, elif e else: entendendo o fluxo do interpretador em condicionais
"""
condicao1 = True
condicao2 = False

if condicao1:
    print('Eu sou verdadeiro')
elif not condicao2:
    print('Eu sou falso')
else:
    print('Eu sou falso')

if 10 == 10:
    print('Outro if')

print('Fora do if')