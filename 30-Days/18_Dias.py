"""
1 - 4 Entradas
    - Quantidade de alunos
    - Nome do aluno
    - Nota do aluno
    - Aluno que deseja remover
2 - 2 saídas
    - Quando a função retornar True deve exibir a mensagem "Aluno removido com sucesso"
    e se retornar False a mensagem "Aluno não encontrado" junto com o dicionario final
3 - Ela deve receber:
    - Um dicionário de alunos;
    - O nome do aluno.
    Ela deve:
    - Remover o aluno do dicionário, caso ele exista;
    - Retornar True caso a remoção seja realizada;
    - Retornar False caso o aluno não exista.
A função deve modificar o próprio dicionário recebido.

4 - O programa principal deve:
    - Perguntar quantos alunos serão cadastrados.
    - Receber nome e nota de cada aluno.
    - Perguntar qual aluno deseja remover.
    - Chamar a função.
    - Exibir:
        "Aluno removido com sucesso" quando retornar True;
        "Aluno não encontrado" quando retornar False.
    - Exibir o dicionário final.
5 -
Receber quantidade

↓

Cadastrar alunos

↓

Receber aluno que será Removido


↓

Chamar remover_aluno()

↓

Exibir mensagem

↓

Exibir dicionário

6 - Receber quantidade

↓

Cadastrar alunos
↓
Exibir mensagem

↓

Exibir dicionário
"""


def atualizar_nota(dicionario_alunos, nome_aluno):
    if nome_aluno in dicionario_alunos:
        del dicionario_alunos[nome_aluno]
        return True
    else:
        return False


quantidade_alunos = int(input("Quantidade de alunos: "))

alunos_cadastrados = {}
for _ in range(quantidade_alunos):
    nome = input("Nome: ").lower()
    alunos_cadastrados[nome] = float(input("Nota: "))

aluno = input("Aluno: ").lower()

resultado = atualizar_nota(alunos_cadastrados, aluno)
if resultado:
    print("Aluno removido com sucesso")
else:
    print("Aluno não encontrado")
print(alunos_cadastrados)
