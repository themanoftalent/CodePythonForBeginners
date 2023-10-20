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

#This is about frozenset
#A frozenset is an immutable set.
# You cannot add or remove elements from a frozenset after it is created.
# You can perform non-modifying operations on a frozenset.
# Create a frozenset

# Create a frozenset
fruits = frozenset(["apple", "banana", "cherry"])

# Attempt to add an element (this will raise an error)
# fruits.add("orange")

# Attempt to remove an element (this will raise an error)
# fruits.remove("apple")

# Non-modifying operations are allowed
if "apple" in fruits:
    print("Apple is in the frozenset.")

# Iterating over the frozenset
for fruit in fruits:
    print(fruit)

