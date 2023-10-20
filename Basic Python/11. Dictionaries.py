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

# Create a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# Accessing values by key
print(dictionary["cat"])  # Output: chat
print(dictionary["dog"])  # Output: chien

# Modifying values
dictionary["cat"] = "le chat"  # Change the value associated with the key "cat"
print(dictionary["cat"])  # Output: le chat

# Adding new key-value pairs
dictionary["fish"] = "poisson"
print(dictionary)  # Output: {'cat': 'le chat', 'dog': 'chien', 'horse': 'cheval', 'fish': 'poisson'}

# Removing a key-value pair
del dictionary["horse"]
print(dictionary)  # Output: {'cat': 'le chat', 'dog': 'chien', 'fish': 'poisson'}

# Checking if a key exists
if "dog" in dictionary:
    print("The key 'dog' exists in the dictionary.")
