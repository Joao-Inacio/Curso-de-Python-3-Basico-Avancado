n = int(input())
arr = map(int, input().split())

lista = list(arr)
maior = lista[0]
segundo_maior = None

for i in lista:
    if i > maior:
        segundo_maior = maior
        maior = i
    elif i < maior:
        if segundo_maior is None or i > segundo_maior:
            segundo_maior = i

print(segundo_maior)

