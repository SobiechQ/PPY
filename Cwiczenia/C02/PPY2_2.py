# wyniki wypisz na konsoli

# 2A.
# Wypisz 10 następnych liczb naturalnych od wskazanej liczby (wyłącznie). 
# Przykład, number = 5, wyświetl od 5 do 14

# 2B. 
# Napisz program, który będzie zwracał tabliczkę mnożenia (do 20.) dla podanej liczby 
# UWAGA - w dwóch kolumnach, moe być w podziale parzyste/nieparzyste

# 2C.
# pobierz od użytkownika liczbę (pomińmy sprawdzanie czy to liczba, póki co...)
# dodaj do niej wszystkie liczby w zakresie od 0 do tej liczby (włącznie!)
number = int(input("Enter a number: "))
if number >= 0:
    for i in range(number + 1, number + 11):
        print(i, end=" ")
print("\n=================================")
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i * j, end=" | ")
    print()
print("\n=================================")
number = int(input("Enter a number: "))
for i in range(0, number + 1):
    number += i
print(number)
