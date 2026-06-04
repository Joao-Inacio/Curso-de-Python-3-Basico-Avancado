"""
1 - As entradas serão três notas sedo que cada uma estará no intervalo de 0 a 10
2 - A Saida será a media das três notas de entrada resultando em valor do tipo float
junto com um mensagem com condição baseado na média sendo:
    Média < 5 -> Reprovado
    Média >= 5 e < 7 -> Recuperação
    Média >= 7 -> Aprovado
3 - receber as 3 notas com pontos flutuantes usando 3 variáveis
a média será outra variável com a soma de todas as 3 notas dividida por 3
passando esse valor para condicional retornado o a média final e a mensagem
"""
nota_1 = float(input("Digite a Nota 1: "))
nota_2 = float(input("Digite a Nota 2: "))
nota_3 = float(input("Digite a Nota 3: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 5:
    print(f"Situação: Reprovado \nSua média foi {media:.1f}")
# elif media >=5 and media < 7:
#     print(f"Situação: Recuperação \nSua média foi {media:.1f}")
elif 5 <= media < 7:
    print(f"Situação: Recuperação \nSua média foi {media:.1f}")
else:
    print(f"Situação: Aprovado \nSua média foi {media:.1f}")


