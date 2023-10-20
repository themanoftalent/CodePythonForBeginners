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
    x=int(input("enter a num"))
    if(x>10000):
        print("enter less than 10000")
    sum=0
    a=x
    while (a>0):
        dig=a%10
        sum+=dig**3
        a//=10
    if x==sum:
        print("yes")
    else:
        print("no")
except:
    print("Invalid input")
