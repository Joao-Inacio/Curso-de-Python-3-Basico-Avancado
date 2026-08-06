"""
1 - 4 entradas
    - Quantidade de Alunos
    - Nome do aluno
    - Idade do Aluno
    - Nota do Aluno
2 - 3 saídas
    - Quantidade de alunos cadastrado
    - Média da turma
    - Quantidade de alunos Aprovados
3 - Ela deve receber:
        - Um dicionário contendo os alunos cadastrados.
    Ela deve retornar uma tupla contendo, nesta ordem:
        - Quantidade de alunos cadastrados.
        - Média das notas.
        - Quantidade de alunos aprovados (nota maior ou igual a 7).
    Importante: Se não houver nenhum aluno cadastrado, a média deve ser 0.
    A função não deve imprimir nada.
4 - O programa principal deve:
    - Perguntar quantos alunos serão cadastrados.
    - Receber nome, idade e nota de cada aluno.
    - Armazenar os alunos em um dicionário.
    - Chamar gerar_relatorio.
    - Exibir o relatório no formato:
        - Quantidade de alunos: 5
        - Média da turma: 7.8
        - Aprovados: 3
5 -
Receber quantidade

↓

Chamar cadastrar_alunos()

↓

Chamar gerar_relatorio()

↓

Exibir o relatório
        - Quantidade de alunos cadastrados.
        - Média das notas.
        - Quantidade de alunos aprovados (nota maior ou igual a 7).
            Importante: Se não houver nenhum aluno cadastrado, a média deve ser 0.
6 - A função de cadastrar e a logica dos dias 12, 13 e 14
"""


def gerar_relatorio(dicionario_alunos):
    media = 0
    aprovados = 0
    for _, informacoes in dicionario_alunos.items():
        nota = informacoes["nota"]
        media += nota
        if nota >= 7:
            aprovados += 1
    if len(dicionario_alunos) == 0:
        return len(dicionario_alunos), media, aprovados
    return len(dicionario_alunos), (media / len(dicionario_alunos)), aprovados


def cadastrar_alunos(quantidade_alunos):
    alunos_cadastrados = {}
    for _ in range(quantidade_alunos):
        nome = input("Nome: ").lower()
        idade = int(input("Idade: "))
        nota = float(input("Nota: "))
        alunos_cadastrados[nome] = {"idade": idade, "nota": nota}
    return alunos_cadastrados


quantidade_alunos = int(input("Quantidade de alunos: "))

alunos_cadastrados = cadastrar_alunos(quantidade_alunos)
quantidade, media, aprovados = gerar_relatorio(alunos_cadastrados)
print(
    f"Quantidade de alunos: {quantidade}\nMédia da turma: {media}\nAprovados: {aprovados}"
)
