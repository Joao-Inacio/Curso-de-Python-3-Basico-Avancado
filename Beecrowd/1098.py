"""
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""
d2 = 8
for i in range(1, 10, 2):
    for j in  range(1, 4):
        d2 -= 1
        print(f'I={i} J={d2}')
    if d2 == 5:
        d2 = 8

