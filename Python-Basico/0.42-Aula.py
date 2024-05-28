"""
    while - Qual letra apareceu mais vezes na frase? 
    (Iterando strings com while)
"""
frase = "O python é uma linguagem de programação"

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""
while i < len(frase):
    letra = frase[i]
    if letra == " ":
        i += 1
        continue
    quantidade = frase.count(letra)
    if quantidade > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = quantidade
        letra_apareceu_mais_vezes = letra
    print(f"{letra} = {quantidade}")
    i += 1

print(f"A letra que apareceu mais vezes foi '{letra_apareceu_mais_vezes}'")
