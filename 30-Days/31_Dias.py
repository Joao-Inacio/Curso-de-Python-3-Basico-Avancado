def ler_idade():
    while True:
        idade = input()
        try:
            int_idade = int(idade)
            if 0 <= int_idade <= 120:
                return int_idade
            else:
                print("Idade inválida! Digite um valor entre 0 e 120.")
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números inteiros.")

ler_idade()



