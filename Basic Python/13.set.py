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

#This is about set
#A set is an unordered collection of unique elements.
#You can add and remove elements from a set.


# Create a set
fruits = {"apple", "banana", "cherry"}

# Add elements to the set
fruits.add("orange")
fruits.add("apple")  # Adding a duplicate element does not change the set

# Remove elements from the set
fruits.remove("banana")

# Check if an element is in the set
if "cherry" in fruits:
    print("Cherry is in the set.")

# Iterate over the set
for fruit in fruits:
    print(fruit)

# Create a set from a list
colors = set(["red", "green", "blue"])

# Performing set operations (union, intersection)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Union of sets
intersection_set = set1 & set2  # Intersection of sets
