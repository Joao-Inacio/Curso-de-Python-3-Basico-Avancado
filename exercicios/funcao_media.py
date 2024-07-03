# def avg(a=1, *args):
#     for i in args:
#         a += i
#     return a / (len(args) + 1)

# Python: average function
def avg(*args):
    total_sum = sum(args)
    total_count = len(args)
    return total_sum / total_count if total_count != 0 else 0  # Evita divisão por zero

# Testando a função com a sequência fornecida
print(avg(2,5))  # Deve retornar -5.98

