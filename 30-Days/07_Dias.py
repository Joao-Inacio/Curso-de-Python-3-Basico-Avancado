"""
1 - Entrada será duas notas
2 - Saida será a média e a situação do aluno
3 - A função será responsavel por retornar a situação do aluno
4 - o calculo da media deve ficar fora pois a função será usando em outras partes do sistemas
5 - Entrada -> recebe as notas
    Processamento -> calculo da média e passa para a função
    Saida -> exibir o retorno da função com a situação do aluno
"""

def verificar_situacao(media):
    resultado = ""
    if media < 5:
        resultado = "Reprovado"
    elif media >=5 and media < 7:
        resultado = "Recuperação"
    else:
        resultado = "Aprovado"
    return resultado

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
media = (nota_1 + nota_2) / 2
print(f"Média {media}\nSituação: {verificar_situacao(media=media)}")
