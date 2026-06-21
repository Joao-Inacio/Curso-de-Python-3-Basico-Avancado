"""
1 - Será duas notas
2 - Será a média e a situação do aluno
3 - Ela irá receber as duas notas e retornar a média
4 - Ela irá receber a média e retornara a situação do aluno
5 - Recebe as nota
    chama a função de calcular a média
    chama a função de verificar a situação passando o retorno da função de calcular a média
    Por fim será exibido a média e a situação do aluno
"""


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(funcao, nota1, nota2):
    media = funcao(nota1, nota2)
    if media >= 7:
        return f"Média: {media}\nSituação: Aprovado"
    elif media >= 6 and media < 7:
        return f"Média: {media}\nSituação: Recuperação"
    else:
        return f"Média: {media}\nSituação: Reprovado"


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
print(verificar_situacao(calcular_media, nota1=nota1, nota2=nota2))
