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
    print('a\'nin degeri :', a)

    print('###############################') 
    #iterate through all the items in tuple
    for odd_numbers in numbers:
        print('single_item degeri', odd_numbers)
    print('#############################') 
    #iterate through all the items in dictionary    
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,3,5,7,9,11,13,15,Hakan=3400,Ismail=4100,Muhsin=5500,Mehmet=3100,Humeyra=3110,Kubilay=5100))

