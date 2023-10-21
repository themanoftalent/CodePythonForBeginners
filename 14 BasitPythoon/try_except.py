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
try:
    bolunen = int(input('Enter a number'))
    bolen = int(input('Enter another number  '))
    result = bolunen / bolen
    print('bolunen/bolen')
except ValueError:
    print('Enter a number')


except ZeroDivisionError:
    print("0 ile bolunme sorunu, hata divided by zero!, 404 anan")
