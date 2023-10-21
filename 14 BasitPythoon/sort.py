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
    n=int(input("Enter max elements in array:"))
    if(n>1000):
        print("more than 1000")
    a=[int(input()) for i in range(n)]
    list.sort(a)
    print(*a)
except:
    print("Invalid entry")
