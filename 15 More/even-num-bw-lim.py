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
    x=int(input("Enter the lower limit for the range:"))
    y=int(input("Enter the upper limit for the range:"))
    for i in range(x,y):
        if(i%2==0):
            print (i)
        elif(x==(y-x)):
            print("no even number in this limit")
except:
    print("Invalid entry")
