"""
1 - 4 entradas
    - Quantidade de alunos e notas
    - Nome do aluno
    - Nota do aluno
    - Nome do aluno que será usado para consultar
2 - 1 saída
    - Nota do aluno se estiver cadastrado ou a mensagem de "Aluno não encontrado" se não estiver cadastrado
3 - Ela deve receber:
    - um dicionário contendo os alunos;
    - o nome do aluno.
    - deve retornar:
    - a nota do aluno, caso ele exista
    - a mensagem "Aluno não encontrado" caso o nome não esteja cadastrado.
4 - O programa deve:
    - Perguntar quantos alunos serão cadastrados.
    - Receber nome e nota de cada aluno e armazená-los em um dicionário.
    - Perguntar qual aluno deseja consultar.
    - Chamar a função.
    - Exibir o resultado.
5 - - Receber a quantidades de alunos que serão cadastrados.

↓
Receber nome e nota de cada aluno e armazená-los em um dicionário.

↓

Chamar a função e passando o dicionário

↓

Usar um if para ver se contem o nome no dicionário como chave

↓
Caso ele exista ela deve retornar a nota do aluno e caso o nome não esteja cadastrado ela deve retorna a mensagem "Aluno não encontrado"

↓

Exibir o retorno da função "consultar_nota"
"""


def consultar_nota(dicionario_alunos, nome_aluno):
    return dicionario_alunos.get(nome_aluno, "Aluno não encontrado")


quantidade_alunos = int(input("Quantidade de alunos: "))

alunos_cadastrados = {}
for _ in range(quantidade_alunos):
    nome = input("Nome: ").lower()
    alunos_cadastrados[nome] = float(input("Nota: "))

consulta = input("Consultar: ").lower()
resultado = consultar_nota(alunos_cadastrados, consulta)
print(f"Nota: {resultado}")
