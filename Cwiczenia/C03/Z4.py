# -*- coding: utf-8 -*-
"""
Stwórz listę tupli, gdzie każda tupla zawiera informacje o produkcie: nazwę, cenę i kategorię. 
#Przykład
products = [
    ("Laptop", 1500, "Elektronika"),
    ("Kubek", 10, "Dom"),
    ("Słuchawki", 100, "Elektronika"),
    ("Sok", 5, "Żywność"),
    ("Telefon", 2000, "Elektronika"),
    ("Długopis", 2, "Biuro"),
    ("Papier", 10, Biuro),
    ("Koszulka", 20, "Moda"),
    ("Pomarańcza", 5,"Żywność" )
]

Utwórz set zawierający wszystkie unikalne kategorie produktów.
Oblicz średnią cenę produktów oraz średnią cene produków z danej kategorii.
Znajdź najdroższy i najtańszy produkt oraz najdroższy i najtańszy produkt z danej kategorii.
Stwórz listę zawierającą nazwy wszystkich produktów o cenie powyżej 100 zł.
Wypisz informacje o produktach, których kategoria zaczyna się od litery "E".
"""
from functools import reduce

products = [
    ("Laptop", 1500, "Elektronika"),
    ("Kubek", 10, "Dom"),
    ("Słuchawki", 100, "Elektronika"),
    ("Sok", 5, "Żywność"),
    ("Telefon", 2000, "Elektronika"),
    ("Długopis", 2, "Biuro"),
    ("Papier", 10, "Biuro"),
    ("Koszulka", 20, "Moda"),
    ("Pomarańcza", 5, "Żywność")
]
kategorie = set(map(lambda x: x[2], products))

print(reduce(lambda x, y: x + y, map(lambda x: x[1], products)) / len(products))


def zKategorii(s: str):
    return list(filter(lambda x: x[2] == s, products))

dlaKatrgorii = "Elektronika"
print(reduce(lambda x, y: x + y, map(lambda x: x[1], zKategorii(dlaKatrgorii))) / len(zKategorii(dlaKatrgorii)))
print("==")
print(max(products, key=lambda x: x[1]))
print(min(products, key=lambda x: x[1]))
print("==")
print(max(zKategorii(dlaKatrgorii), key=lambda x: x[1]))
print(min(zKategorii(dlaKatrgorii), key=lambda x: x[1]))

lista = list(filter(lambda x: x[1]>100, products))

print("==")
for e in filter(lambda x: x[2][0] == 'E', products):
    print(e)