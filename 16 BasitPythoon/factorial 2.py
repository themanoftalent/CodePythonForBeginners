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
    n=int(input("Enter a number:"))
    x=1
    for i in range (1,6):
        x=n*i
        print(x)
except:
    print("Invalid Entry")
