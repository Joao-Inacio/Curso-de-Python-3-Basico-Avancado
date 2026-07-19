"""
1 - Serão 3 entradas
    - Quantidade de notas
    - Nome do aluno
    - Nota do aluno
2 - Serão 2 saídas
    - Nome do aluno
    - Nota do aluno
3 - Ela deve:
    - Receber a quantidade de alunos.
    - Solicitar o nome e a nota de cada aluno.
    - Armazenar cada aluno em um dicionário, utilizando o nome como chave e a nota como valor.
    - Retornar o dicionário com todos os alunos cadastrados.
4 - O programa principal deve:
    - Perguntar quantos alunos serão cadastrados.
    - Chamar a função cadastrar_alunos.
    - Exibir todos os alunos cadastrados.
5 - Receber a quantidades de alunos

↓

Chamar a função e passando a quantidade de alunos

↓

Usar um for para inteirar a quantidade e receber os dados (Nome e Nota)

↓
Criar o dicionario e armazenar os dados (Nome e Nota)

↓

Exibir os alunos cadastrados
"""


def cadastrar_alunos(quantidade_alunos):
    alunos_cadastrados = {}
    for _ in range(quantidade_alunos):
        nome = input("Nome: ")
        alunos_cadastrados[nome] = float(input("Nota: "))
    return alunos_cadastrados


quantidade_alunos = int(input("Quantidade de alunos: "))

resultado = cadastrar_alunos(quantidade_alunos)
print("Alunos cadastrados: ")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
