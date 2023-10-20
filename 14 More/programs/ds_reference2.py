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
print("Go shopping and buy the list below.\n")
sholist=["Apple","Onion","Carrot","Mango","Eggs","Banana","Badminton"]

del sholist[0]
sholist.append("Leamon")

print(sholist)
print("--"*35)
#No difference between both as myList points shoplist.
myList=sholist[:]
print(myList)
