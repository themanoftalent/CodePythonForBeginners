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

# If-Else Condition Example in Python
# The 'if' condition is used to check a condition.
# If the condition is true, it executes the code inside the 'if' block.

# Prompt the user to enter a number to check if it's even or odd
user_input = input("Enter a number to check if it's even or odd: ")

# Convert the user input to an integer
number = int(user_input)

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


