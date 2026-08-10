"""
1 - 4 entradas
    - A quantidade de alunos
    - Nome do Aluno
    - Idade do aluno
    - Nota do Aluno
2 - 2 Saídas
    - O dicionario original
    - O novo dicionario contendo as alunos aprovados
3 - Ela deve receber:
    - Um dicionário contendo os alunos cadastrados.
    - Ela deve retornar um novo dicionário contendo apenas os alunos aprovados.
4 - O programa principal deve:
    - Perguntar quantos alunos serão cadastrados.
    - Receber nome, idade e nota.
    - Armazenar os alunos.
    - Chamar filtrar_aprovados.
    - Exibir:
        cadastro original
        alunos aprovados.
5 - Receber quantidade

↓

Chamar cadastrar_alunos()

↓

Chamar filtrar_aprovados()

↓
Exibir cadastro original e alunos aprovados.

6 - posso usar a logica do dia 7, 8 e 10 fazendo algumas melhorias para lidar com o dicionario
"""


def filtrar_aprovados(dicionario_alunos):
    alunos_aprovados = {}
    for nome, informacoes in dicionario_alunos.items():
        idade = informacoes["idade"]
        nota = informacoes["nota"]
        if nota >= 7:
            alunos_aprovados[nome] = {"idade": idade, "nota": nota}
    return alunos_aprovados


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

alunos_aprovados = filtrar_aprovados(alunos_cadastrados)
print(f"Todos os Alunos:\n{alunos_cadastrados}")
print(f"Alunos aprovados:\n{alunos_aprovados}")
