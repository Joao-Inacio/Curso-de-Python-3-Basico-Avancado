"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = ' Python é muito legal, e mais fácil '
frase2 = ' Ótimo para ciência de dados'
lista_palavras = frase.split()
lista_frase = frase.split(',')
print(lista_palavras)
print(lista_frase)
print(frase.strip()) # Corta os espaços 
nova_frase = '-'.join(frase2)
print(nova_frase)


