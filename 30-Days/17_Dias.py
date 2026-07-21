"""
1 - 4 entradas
    - Quantidade de alunos
    - Nome do Aluno
    - Nota do Aluno
    - Nome de qual aluno deseja atualizar
    - A nova nota do aluno
2 - 1 Saída
    - Quando a função retornar True deve exibir a mensagem "Nota atualizada com sucesso"
    e quando retornar False a mensagem "Aluno não encontrado" junto com o o dicionário final.
3 - Ela deve receber:
    - Um dicionário de alunos;
    - O nome do aluno;
    - A nova nota.
    Ela deve:
    - Atualizar a nota do aluno, caso ele exista;
    - Retornar True se a atualização for realizada;
    - Retornar False caso o aluno não esteja cadastrado.
    A função deve modificar o próprio dicionário recebido.
4 -
- O programa deve:
    - Perguntar quantos alunos serão cadastrados.
    - Receber nome e nota de cada aluno.
    - Perguntar qual aluno deseja atualizar.
    - Perguntar a nova nota.
    - Chamar a função.
    - Exibir:
        - "Nota atualizada com sucesso" quando a função retornar True;
        - "Aluno não encontrado" quando retornar False.
    - Exibir o dicionário final.
5 -
Receber quantidade

↓

Cadastrar alunos

↓

Chamar função

↓

Atualizar

↓

Retornar resultado

↓

Exibir
"""


def atualizar_nota(dicionario_alunos, nome_aluno, nova_nota):
    if nome_aluno in dicionario_alunos:
        dicionario_alunos[nome_aluno] = nova_nota
        return True
    else:
        return False


quantidade_alunos = int(input("Quantidade de alunos: "))

alunos_cadastrados = {}
for _ in range(quantidade_alunos):
    nome = input("Nome: ").lower()
    alunos_cadastrados[nome] = float(input("Nota: "))

aluno = input("Aluno: ").lower()
nova_nota = float(input("Nova nota: "))
resultado = atualizar_nota(alunos_cadastrados, aluno, nova_nota)
if resultado:
    print("Nota atualizada com sucesso")
    print(alunos_cadastrados)
else:
    print("Aluno não encontrado")
