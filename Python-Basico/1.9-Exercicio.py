"""
Exercício guiado com while
"""

nome = input("Digite seu nome: ")
tamanho = len(nome)
contador = 0
novo_nome = ''

while contador < tamanho:
    
    print(f'*{nome[contador]}*')
    novo_nome += f'{nome[contador]}*'
    contador += 1

print(novo_nome)
