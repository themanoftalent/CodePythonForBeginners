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

fib_array = [0, 1]


def fib(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        temp_fib = fib(n - 1) + fib(n - 2)
        fib_array.append(temp_fib)
        return temp_fib


print(fib(40))
