# oblicz silnię podanej liczby
from functools import reduce
print(reduce(lambda x, y: x * y, range(1, int(input("Podaj liczbę:\n"))+1)))
