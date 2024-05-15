"""
Faça um programa que solicite o raio de um círculo e calcule a área. 
A fórmula da área do círculo é: Área = π * raio^2. Use o valor de π como 3.14.
"""
raio = input("Insira a área: ")
try:
    area = 3.14 * float(raio) ** 2
    print(f'A ária do circulo é {area}')
except:
    print(f'{raio} não é um raio valido, insira o valor valido')