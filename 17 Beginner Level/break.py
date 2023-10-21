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
for n in range(2, 11):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'equals', x, '*', int(n/x))
            break
    else:
        # loop fell through without finding a factor
        print (n, 'is a prime number')
