# -*- coding: utf-8 -*-

'''
Napisz funkcję slowa_podobne(s, words), która wyświetli słowa, które są ,,podobne" do napisu s
w tym sensie, że składające się z tych samych znaków — ale ewentualnie występujących inną liczbę razy
#PRZYKŁAD
slowa_podobne('one', ['one', 'two', 'none', 'three', 'neon', 'eon']) 
>> none neon eon
'''


def slowa_podobne(s, words: list):
    for e in filter(lambda x: set(x) == set(s), words):
        print(e)


slowa_podobne('one', ['one', 'two', 'none', 'three', 'neon', 'eon'])
