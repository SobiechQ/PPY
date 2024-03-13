# napisz kod, który wyświetli ciąg fibonnaciego do 10 miejsc (https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego)
# pierwsze dwie liczby w ciągu
def fib(n) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print("Ciąg Fibonacciego:")
for i in range(1, 11):
    print(fib(i))
