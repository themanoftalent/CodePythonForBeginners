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

# This is about list slicing
# List slicing is a feature of Python which allows you to create a sublist from a list.
# You can specify the start and end positions of the sublist.
# The syntax for list slicing is as follows:

numbers = [0, 1, 2, 3, 4, 5]
sublist = numbers[1:4]  # Gets elements at index 1, 2, and 3
print(sublist)  # Output: [1, 2, 3]
print("#"*50)
numbers = [0, 1, 2, 3, 4, 5]
sublist_start = numbers[:3]  # Gets elements at index 0, 1, and 2
sublist_end = numbers[2:]    # Gets elements from index 2 to the end
print(sublist_start)  # Output: [0, 1, 2]
print(sublist_end)    # Output: [2, 3, 4, 5]
print("#"*50)
numbers = [0, 1, 2, 3, 4, 5]
sublist = numbers[-3:-1]  # Gets elements at index -3 (3rd from the end) and -2
print(sublist)  # Output: [3, 4]
print("#"*50)
numbers = [0, 1, 2, 3, 4, 5]
sublist = numbers[1:5:2]  # Gets elements at index 1, 3
print(sublist)  # Output: [1, 3]
