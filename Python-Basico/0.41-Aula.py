while True:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite o segundo número: ")
    operacao = input("Escolha um operador [+]Adição, [-]Subtração, [x]Multiplicação, [/]Divisão: ")

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        if operacao == '+':
            print(f'{numero1} + {numero2} = {numero1 + numero2}')
        elif operacao == '-':
            print(f'{numero1} - {numero2} = {numero1 - numero2}')
        elif operacao == 'x':
            print(f'{numero1} x {numero2} = {numero1 * numero2}')
        elif operacao == '/':
            print(f'{numero1} / {numero2} = {numero1 / numero2}')
        else:
            print('Operador inválido!')
    except ValueError:
        print('Valor adicionado não é um número ou operação inválida')

    continua = input("Deseja continuar [S/N]? ").strip().lower()
    if continua == 'n':
        break
