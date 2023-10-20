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
def total(a=5, *numbers, **phonebook):
    print('a sayisi', a)
    print('-'*34)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
        
    #iterate through all the items in dictionary    
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(55,1,2,3,'\n',Jack=44401123,John=5552231,Inge=3331560))
