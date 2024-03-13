"""
A. 
napisz program, którego wynik będzie jak poniżej
Podpowiedź: argumenty, które przyjmuje funkcja range to (start, stop, step)
step przyjmuje domyślnie wartość 1
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""


def inner(i):
    if i < 1:
        return
    print(i, end=" ")
    inner(i - 1)


def outer(i):
    if i < 1:
        return
    inner(i)
    print()
    outer(i - 1)


outer(5)

"""
B. 
Rozszerz powyzszy kod o warunki i dostosuj go do ponieszego wzoru:
11 # 9 -8 7 -6 # -4 3 -2 1 
# 9 -8 7 -6 # -4 3 -2 1 
9 -8 7 -6 # -4 3 -2 1 
-8 7 -6 # -4 3 -2 1 
7 -6 # -4 3 -2 1 
-6 # -4 3 -2 1 
# -4 3 -2 1 
-4 3 -2 1 
3 -2 1 
-2 1 
1 
"""


def minusHash(i):
    if i % 5 == 0:
        return '#'
    if i % 2 == 0:
        return -i
    return i


def inner2(i):
    if i < 1:
        return
    print(minusHash(i), end=" ")
    inner2(i - 1)


def outer2(i):
    if i < 1:
        return
    inner2(i)
    print()
    outer2(i - 1)


for i in map(minusHash, range(0, 10)):
    print(i)

