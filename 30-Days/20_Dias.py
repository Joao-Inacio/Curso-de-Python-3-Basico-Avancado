"""
1 - São 5 entradas
    - Quantidade de alunos
    - Nome do aluno
    - Idade do Aluno
    - Nota do Aluno
    - Nome do aluno para ser pesquisado
2 - A saídas serão
    Se o aluno existir, exibir:
    - Nome do Aluno
    - Idade do Aluno
    - Nota do Aluno
    Caso contrário, exibir:
    - "Aluno não encontrado"
3 - Ela deve receber:
    - Um dicionário de alunos;
    - O nome do aluno.
    Ela deve retornar:
    - Um dicionário de informações do aluno, caso ele exista;
    - None, caso ele não esteja cadastrado.
    Importante: a função não deve imprimir mensagens.
4 - O programa principal deve:
    - Perguntar quantos alunos serão cadastrados.
    - Receber nome, idade e nota de cada aluno.
    - Perguntar qual aluno deseja consultar.
    - Chamar a função.
    - Se o aluno existir, exibir:, Aluno, Idade, Nota
    - Caso contrário, exibir: "Aluno não encontrado"
5 -
Receber quantidade

↓

Receber  Nome do aluno, Idade do aluno, Nota do aluno

↓

Receber  Nome do aluno que deseja consultar.

↓
Chamar a função e passando o dicionário

↓

Exibir dicionário se o aluno existir, caso contrário, exibir: "Aluno não encontrado"

6 - Usa a função o conteúdo da função cadastrar_alunos do dia 19 e a complementa a logica do dia 16
"""


def consultar_aluno(dicionario_alunos, nome_aluno):
    return dicionario_alunos.get(nome_aluno)


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

consulta = input("Consultar: ").lower()
resultado = consultar_aluno(alunos_cadastrados, consulta)

if resultado:
    print(f"Nome: {consulta}\nIdade: {resultado['idade']}\nNota: {resultado['nota']}")
else:
    print("Aluno não encontrado")
