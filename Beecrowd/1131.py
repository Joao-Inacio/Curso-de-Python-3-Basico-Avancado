inter = 0
gremio = 0
empate = 0
grenal = 0
conti = 0
while conti != 2:
    inte, gremi = input().split()
    inte = int(inte)
    gremi = int(gremi)
    if inte > gremi:
        inter += 1
    elif gremi > inte:
        gremio += 1
    elif gremi == inte:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    conti = int(input())
    grenal += 1

print(f'{grenal} grenais')
print(f'Inter: {inter}')
print(f'Gremio: {gremio}')
print(f'Empates: {empate}')
if gremio > inter:
    print(f'Gremio venceu mais')
else:
    print(f'Inter venceu mais')
