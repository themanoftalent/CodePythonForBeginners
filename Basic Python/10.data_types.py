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



# Creating a list with elements of different data types
data = [1, "apple", 3.14, "banana", True, [5, 6, 7], (8, 9)]

# Slicing to get sublists with specific data types
strings = data[1:4]  # Gets elements at index 1, 2, and 3 (strings)
numbers = data[0:1]  # Gets elements at index 0 (integer)
floats = data[2:3]   # Gets elements at index 2 (float)
booleans = data[4:5] # Gets elements at index 4 (boolean)
lists = data[5:6]    # Gets elements at index 5 (list)
tuples = data[6:]    # Gets elements at index 6 (tuple)

# Printing the sublists
print("Strings:", strings)   # Output: ['apple', 3.14, 'banana']
print("Numbers:", numbers)   # Output: [1]
print("Floats:", floats)     # Output: [3.14]
print("Booleans:", booleans) # Output: [True]
print("Lists:", lists)       # Output: [[5, 6, 7]]
print("Tuples:", tuples)     # Output: [(8, 9)]
