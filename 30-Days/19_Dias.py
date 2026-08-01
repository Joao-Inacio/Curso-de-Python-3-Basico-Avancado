"""
1 - 4 entradas
    - Quantidade de alunos
    - Nome do aluno
    - Idade do aluno
    - Nota do aluno
2 - Serão Exibido todos os alunos cadastrados no formato:
    - Aluno
    - Idade
    - Nota
3 - Ela deve receber:
    - A quantidade de alunos.
    Ela deve:
    - Solicitar o nome;
    - Solicitar a idade;
    - Solicitar a nota;
    - Armazenar essas informações em um dicionário aninhado;
    - Retornar o cadastro completo.
4 - O programa principal
    - Perguntar quantos alunos serão cadastrados.
    - Chamar a função.
    - Exibir todos os alunos cadastrados
5 -
Receber quantidade

↓

Receber  Nome do aluno, Idade do aluno, Nota do aluno

↓

Chamar cadastrar_alunos()

↓

Exibir dicionário
"""


def cadastrar_alunos(quantidade_alunos):
    alunos_cadastrados = {}
    for _ in range(quantidade_alunos):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        nota = float(input("Nota: "))
        alunos_cadastrados[nome] = {"idade": idade, "nota": nota}
    return alunos_cadastrados


quantidade_alunos = int(input("Quantidade de alunos: "))

resultado = cadastrar_alunos(quantidade_alunos)
for nome, informacoes in resultado.items():
    idade = informacoes["idade"]
    nota = informacoes["nota"]
    print(f"Aluno: {nome}\nIdade: {idade}\nNota: {nota}")
