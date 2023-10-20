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


# **kwargs allows you to pass a variable number of keyword arguments to a function.
def greet(**kwargs):
    if "name" in kwargs and "age" in kwargs:
        return f"Hello, {kwargs['name']}! You are {kwargs['age']} years old."
    else:
        return "Hello, there!"

# Call the function with different keyword arguments
message1 = greet(name="Alice", age=25)
message2 = greet(name="Bob")

print(message1)  # Output: Hello, Alice! You are 25 years old.
print(message2)  # Output: Hello, there!
