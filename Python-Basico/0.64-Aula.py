"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 <= 11
variavel  = 'valor' if condicao else 'Outro valor'
print(variavel)
print('Valor' if True else 'Outro valor')

digito = 0
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

