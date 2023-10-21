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
x = 50 #gloabl variable is defined


def func():
    global x #assign global value

    print('Global x is', x)
    x = 2
    print('Changed global x to', x,'making it local')


func()
print('Value of x is', x)
