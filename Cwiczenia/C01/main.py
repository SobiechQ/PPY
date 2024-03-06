# val = input("Podaj imie: ")
# print("Witaj! "+val)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista += "a"
print(lista)
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple += (10, 20)
print(tuple)
min = (160,)
print(min)
stawka, godziny = input("Podaj stawke i godziny").split()
stawka, godziny = int(stawka), int(godziny)
wynagrodzenie = 0


if godziny > min[0]:
    wynagrodzenie = (godziny - min[0]) * stawka/2
wynagrodzenie += stawka * godziny
print(wynagrodzenie)




wiek = int(input("Podaj wiek: "))

if wiek > 120:
    print("Za wiele")
elif wiek > 18:
    print("dorosly")
elif wiek > 0:
    print("dzieciak")
elif wiek == 0:
    print("kaszojad")
elif wiek < 0:
    print("niepoprawny")

divide = float(input("Podaj liczbe"))
print("Podzielna" if divide % 7 == 0 else "Niepodzielna")

triple = (float(input("a: ")),
          float(input("b: ")),
          float(input("c: ")))
delta = (triple[1] ** 2) - 4 * triple[0] * triple[2]
print("Brak rozwiązań" if delta < 0 else "Jedno rozwiązanie" if delta == 0 else "Dwa rozwiązania")


