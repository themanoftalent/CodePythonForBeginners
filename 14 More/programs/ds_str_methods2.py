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
names = "Akifhan"
if "n" in names:
    print ('Yes there is n')
if names.startswith ("A"):
    print ('True, it starts with A')

if names.find ('han') != -1:
    print ('Akifhan names contain han')
print ('\n')
#listeyi birlestir man
delimeter = '_*_'
myList=['Russia','Brasil,England','Enemeies','Big Picture']
print(delimeter.join(myList))
