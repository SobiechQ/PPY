import math

x = math.factorial(1000)
# sep = separator
print('a', 'b', 'c', sep=':', end=" koniec lini \n")
print("a" + str(10))
print(type(x), "   ", x)
compl1 = 2 - 3j
compl2 = 4 + 1j
try:
    print(compl1 > compl2)
except TypeError:
    print("no nie bardzo")
print(compl1)

# indentyfikator obiektu reprezentującego
print(id(x))
for i in (30, 20, 10):
    print(i)
for i in [30, 20, 10]:
    print(i)
for i in range(10, 20, 2):
    print(i)
for i in range(20, 15, -1):
    print(i)
lista = [1, 2, 3]
lista2 = [10, 20]
lista3 = lista

lista3.append(lista2)
print(lista)
print(lista3)
# lista jest modyfikowalna

# tuple jest niemodyfikowalny
tup = (10, "test", 20)
# tup[0] = 20 nie mozna bo zmiana
tup2 = (0, 1, [10, 20])
tup2[2].append(30)
print(tup2)

range = range(2, 12, 2)
print(range)

del lista3[0]
lista3.extend(lista2)
print(lista3)
niemodyfikowalne = 10
print(id(niemodyfikowalne))
niemodyfikowalne += 10
print(id(niemodyfikowalne))

mySet1 = {10, 20, 30}
mySet2 = {40, 50}
print((mySet1 | mySet2))  # set dzialaja jak hashset

# dict dziala jak linkedHashMap
myDict = {"raz": 1, "dwa": 2, "trzy": [1, 2]}
print(myDict["raz"])
print(myDict)
