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
#edited for python 3 and some basic arrangments
#!editor :Barish


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = fib(100)

# Iterating over the generator object using next
print(x.__next__()); # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for in loop.
print("\nUsing for in loop")
for i in fib(100):
    print(i),
