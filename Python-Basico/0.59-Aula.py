"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

from decimal import Decimal
from math import ceil

n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print(n3)

print(ceil(n3))
print(round(n3, 2))
print(Decimal(0.1 + 0.7))
