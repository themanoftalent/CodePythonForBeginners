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
    n=int(input("enter limit:"))
    a=int(input("enter starting num:"))
    d=int(input("enter common diff:"))
    sum=(n/2)*((2*a)+(n-1)*d)
    print(sum)
except:
    print("Invalid entry")
