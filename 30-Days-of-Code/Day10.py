n = int(input())
binary = bin(n)[2:]
grupy = binary.split('0')
maxm = max(grupy)
print(len(maxm))
