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
    x=int(input("Enter a number:"))
    fact=1
    for i in range (1,x+1):
        fact=fact*i
    print(fact)
except:
    print("Invalid Entry")
