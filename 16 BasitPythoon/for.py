##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################
# edited for python 3 and some basic arrangments
# !editor :Barish
# working with list

words = ['cat', 'window', 'car', 'defenestrate', 'car']
for w in words:
    print(w, len(w))

print(type(words))
words.append('dog')
print(words)

words.remove('cat')
print(words)

words.extend('starbucks')  # extend the word like 's', 't', 'a', 'r', 'b', 'u', 'c', 'k', 's']
print(words)

words.insert(2, 'Stars')  # 0 1 den sonra
print(words)

