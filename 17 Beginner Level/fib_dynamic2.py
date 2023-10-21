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

def fib(n):
    if n==0 or n==1:
        return n
    else:
        a, b = 0, 1
        for i in range(2,n):
            a, b = b, a + b
            # print a, b
        return a+b

print (fib(800))
