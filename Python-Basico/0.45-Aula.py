"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto:
#     print(letra)

texto = 'Python'
texto_iteravel = iter(texto)

print(next(texto_iteravel))
print(next(texto_iteravel))
print(next(texto_iteravel))
print(next(texto_iteravel))
print(next(texto_iteravel))
print(next(texto_iteravel))
