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

# Best practice is best practiced when much practice has been done without consideration for it.

# Creating tuples
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida')
tup2 = (1, 2, 3, 4, 5, 6, 7)

# Accessing elements in tuples
print(tup1[0])  # Output: Robert
print(tup2[1:4])  # Output: (2, 3, 4)

# Packing and Unpacking tuples
x = ("Guru99", 20, "Education")  # Tuple packing
(company, emp, profile) = x  # Tuple unpacking
print(company)  # Output: Guru99
print(emp)  # Output: 20
print(profile)  # Output: Education

# Comparing tuples
# Case 1
a = (5, 6)
b = (1, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# Case 2
a = (5, 6)
b = (5, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# Case 3
a = (5, 6)
b = (6, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# Converting dictionary items to tuples
a = {'x': 100, 'y': 200}
b = a.items()
print(b)  # Output: dict_items([('x', 100), ('y', 200)])

# Slicing a tuple
x = ("a", "b", "c", "d", "e")
print(x[2:4])  # Output: ('c', 'd')
