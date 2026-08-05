"""
1 - 4 entradas
    - Quantidade de alunos
    - Nome do Aluno
    - Idade do Aluno
    - Nota do aluno
2 - Dicionário dos alunos cadastrados. Caso os dados sejam inválidos, apenas exiba: Cadastro inválido
3 - Função 1
    Ela deve receber:
    - Nome;
    - Idade
    - Nota.
    Ela deve retornar:
    - True se:
        o nome não estiver vazio;
        a idade estiver entre 0 e 120;
        a nota estiver entre 0 e 10.
    - False caso qualquer regra seja violada.
    A função não imprime mensagens.
    Função 2
    - Ela deve receber:
        Quantidade de alunos.
    - Ela deve:
        solicitar nome;
        solicitar idade;
        solicitar nota;
        chamar validar_aluno;
        armazenar apenas os alunos válidos;
        retornar o dicionário dos alunos cadastrados.
    - Caso os dados sejam inválidos, apenas exiba:
        Cadastro inválido
    e continue para o próximo aluno.
4 - O programa principal deve:
    - Perguntar quantos alunos serão informados.
    - Chamar cadastrar_alunos.
    - Exibir todos os alunos cadastrados.
5 -
Receber quantidade

↓

Chamar cadastrar_alunos()

↓

Receber nome do aluno para consulta

↓

Chamar validar_aluno()

↓

Se nenhuma das infamações do dicionário não estiver faltando:
    armazenar apenas os alunos válidos

Caso contrário:
    Exibir "Cadastro inválido"
6 - Posso pegar exemplos da função do dia 20 e melhorar a logica do dia 11
"""


def validar_aluno(nome, idade, nota):
    if nome != "" and idade >= 0 and idade <= 120 and nota >= 0 and nota <= 10:
        return True
    else:
        return False


def cadastrar_alunos(quantidade_alunos):
    alunos_cadastrados = {}
    for _ in range(quantidade_alunos):
        nome = input("Nome: ").lower()
        idade = int(input("Idade: "))
        nota = float(input("Nota: "))
        if validar_aluno(nome, idade, nota):
            alunos_cadastrados[nome] = {"idade": idade, "nota": nota}
        else:
            print("Cadastro inválido")

    return alunos_cadastrados


quantidade_alunos = int(input("Quantidade de alunos: "))

alunos_cadastrados = cadastrar_alunos(quantidade_alunos)
print(alunos_cadastrados)
