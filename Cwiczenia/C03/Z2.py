# -*- coding: utf-8 -*-
'''

Napisz definicje, która przeprowadzi analizę tekstu. Program powinien wykonać następujące czynności:
- Wczytać tekst
- Podzielić tekst na słowa.
- Usunąć znaki interpunkcyjne i zamienić wszystkie litery na małe litery.
- Utworzyć kolekcję słów i zliczyć ile razy każde słowo występuje w tekście.
- Wyświetlić 10 najczęściej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić 10 najrzadziej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić liczbę unikalnych słów w tekście.
- Wyświetlić średnią długość słowa w tekście.
'''
from functools import reduce

with open("Z2_txt.txt", encoding="UTF-8") as file:
    lines = file.readlines()
wordList = []
for line in lines:
    for word in line.split(' '):
        wordList.append(word)

wordCount = {}

for word in map(lambda x: ''.join(filter(str.isalpha, x)).lower(), wordList):
    if not word in wordCount:
        wordCount[word] = 0
    wordCount[word] += 1
print(wordCount)

for item in sorted(wordCount.items(), key=lambda x: -x[1])[:10]:
    print(item)

for item in sorted(wordCount.items(), key=lambda x: x[1])[:10]:
    print(item)

print("Jest: [", len(wordCount.keys()), "] unikalnych wyrazów", sep='')

print(reduce(lambda x,y:x+y, map(lambda x: len(x), wordCount.keys()))/ len(wordCount))
