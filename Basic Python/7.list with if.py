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


#List comprehensions in Python are a concise way to create lists. 
#Create a list of squared numbers from 0 to 9.
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
print("#"*50)
#Create a list of even numbers from 0 to 9.
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
print("#"*50)
#Create a list of odd numbers from 0 to 9.
odd_numbers = [x for x in range(10) if x % 2 == 1]
print(odd_numbers)
print("#"*50)
#Create a list of numbers from 0 to 9, subtracted by 1.
subtracted_numbers = [x - 1 for x in range(10)]
print(subtracted_numbers)
print("#"*50)
#Create a list of the square roots of even numbers from 0 to 9 using the math module.
import math
square_roots = [math.sqrt(x) for x in range(10) if x % 2 == 0]
print(square_roots)
print("#"*50)
#Create a list from a set of unique elements.
set_of_unique_elements = [x for x in set([1, 1, 2, 2])]
print(set_of_unique_elements)
print("#"*50)
