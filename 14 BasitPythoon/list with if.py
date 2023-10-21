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
listone = [2, 3, 4]
#listtwo = [2*i for i in listone if i > 2]

listtwo = [2*i for i in listone]  
"""We dont have to use if we dont want to shwo a condition"""
print(listtwo)
print('#######################')

thisislist1=[3,4,5]
thisislist2=[thisislist1*i for i in thisislist1 if i>4]
print(thisislist2)
print('#######################')

thisislist1=[3,4,5,6,7,8,9,12]
thisislist2=[i*i for i in thisislist1 if i>4]
print(thisislist2)

print('#######################')

thisislist1=[3,4,5,6,7,8,9,12,15,3125]
thisislist2=[i**i for i in thisislist1 if i>4]
print(thisislist2)
