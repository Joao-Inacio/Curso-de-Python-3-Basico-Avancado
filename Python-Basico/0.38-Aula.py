"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0
while contador <= 100:
    contador += 1
    print(contador)

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue
    print('Continuando...')
    
    if contador == 40:
        break
