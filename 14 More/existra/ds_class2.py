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

import sys


#
# print(factorial(123))

# hard way

def de_fact(any_number):
    if any_number == 1:
        return 1
    else:
        return (any_number * (de_fact (any_number - 1)))



de_fact(1)
number = int (input ('Enter a number to calculate factorial : '))
print ('The result of fcu***g number', number, 'factorial is', de_fact (number))



