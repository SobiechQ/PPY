a = 1


def x(b):
    return b + 1


b = a + 2
a += 10

print(x(2))

print(id(a), id(b))
print(a, b)

s1 = "Hello World"
s2 = "Hello World"  # literały będą miały ten sam adres domyślnie, jak w javie

s2 += "1"
s1 += "1"
print(s1 is s2)  # porównanie adresów, odpowiednik == dla obiektów w javie
print(s1 == s2)  # Porównuje wartości

print(x.__str__())
x.__name__ = 'Mozna zmienic nazwe'
print(x.__name__)
print(x.__dir__())

# import nie tylko wczytuje ale również wykonuje wczytany plik py
from math import factorial  # takie using namespace albo import javovy

print(factorial(10))
print(help(b))
for i in range(1, 10):
    pass  # nic nie robi

# raise Exception

# While brake
# brake wykona się zawsze wtedy kiedy wyszedłem z while nie napotykając brake
# tak samo w for

# w foreach może być dowoly obiekt który posiada metodę __iter__
# __iter__ nie ma has next tylko next, jak nie ma to for obsługuje wyjątek

test = (10, 20, 30)
iter = test.__iter__()
print(next(iter))
print(next(iter))
print(next(iter))
# print(next(iter)) #exception

map = {"a": 1, "b": 2}
for key, value in map.items():
    print(key, value)
for obj in map:
    print(obj)  # domyslnie po kluczach

list = [2, 3, 1, 3, 1, 4, 1, 2, 3]
for i in enumerate(list):
    print("enumerator:", i)
