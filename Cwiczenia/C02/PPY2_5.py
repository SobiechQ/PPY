# napisz program, który zwróci wszystkie liczby pierwsze dla wybranego zakresu
# Podpowiedź - znajdź warunki, które eliminują kryteria liczby pierwszej.
from math import isqrt

start = 25
end = 55
print("Liczby pierwsze pomiędzy", start, "i", end, "to:")


def isPrime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


for i in filter(isPrime, range(start, end)):
    print(i)
