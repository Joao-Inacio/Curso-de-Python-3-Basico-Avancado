"""
Faça uma lista de comprar com lista
O usuário deve ter a possibilidade de
inserir, apagar e lista valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
lista = []
try:
    while True:
        print('Selecione uma opção')
        opcao = str(input('[i]nserir [a]pagar [l]istar: '))
        if opcao.upper() == 'I':
            valor = str(input('Valor: '))
            lista.append(valor)
        elif opcao.upper() == 'A':
            opcao = int(input('Indice do que deseje apagar: '))
            if len(lista) > 0:
                del lista[opcao]
            else:
                print('Valor ausente')
        elif opcao.upper() == 'L':
            for indice, nome in enumerate(lista):
                print(indice, nome) 
        else:
            print('\nOpção Invalido\n')
except:
    print('Valor invalido')