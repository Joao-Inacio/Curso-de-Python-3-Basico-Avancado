# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
respostas_certas = 0
respostas_erradas = 0

for pergunta in perguntas:
    print(f"\n{pergunta['Pergunta']}")
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i}) {opcao}")
    
    resposta = int(input('Sua resposta: '))
    if pergunta['Opções'][resposta] == pergunta['Resposta']:
        print('\nVocê acertou')
        respostas_certas += 1
    else:
        print('\nVocê errou')
        respostas_erradas += 1
print(f'Você acertou {respostas_certas}')
print(f'Você Errou {respostas_erradas}')
