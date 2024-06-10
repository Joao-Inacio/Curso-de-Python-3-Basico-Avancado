"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# palavra_secreta = "Sucesso"
# tentativas = 0
# resposta = '*'*len(palavra_secreta)

# while True:
#     try:
#         palavra = str(input("Digite uma palavra: "))
#         tentativas += 1
#         if len(palavra) > 1 or palavra.isnumeric():
#             print('Digite uma palavra valida')
#             continue
#         for i in palavra_secreta:
#             if palavra == i:
#                 resposta[i] += palavra
#         print(resposta)
#     except:
#         print('Error')

palavra_secreta = "sucesso"
tentativas = 0
resposta = ['*'] * len(palavra_secreta)

while True:
    letra = input("Digite uma letra: ").lower()
    tentativas += 1

    if len(letra) != 1 or not letra.isalpha():
        print('Digite uma letra válida.')
        continue

    if letra in palavra_secreta:
        for idx, char in enumerate(palavra_secreta):
            if char == letra:
                resposta[idx] = letra

    print(''.join(resposta))

    if '*' not in resposta:
        print(f'Parabéns! Você adivinhou a palavra secreta "{palavra_secreta}" em {tentativas} tentativas.')
        break

