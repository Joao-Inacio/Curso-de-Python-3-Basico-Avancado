nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios')
else:
    print(f"""
        Seu nome é {nome}
        Seu nome invertido é {nome[::-1]}
        Seu nome contém {' ' in nome} espaços
        Seu nome tem {len(nome)} letras
        A primeira letra do seu nome é {nome[0]}
        A ultima letra do seu nome é {nome[-1]}
    """)