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

# Basic Input and Output Example in Python

# Getting user input
name = input("Enter your name: ")  # Prompt the user for their names

# Display a greeting
print("Hello, " + name + "!")  # Print a greeting with the user's name

# Perform a simple calculation
num1 = float(input("Enter a number: "))  # Prompt the user for a number (as a float)
num2 = float(input("Enter another number: "))  # Prompt the user for another number (as a float)
result = num1 + num2  # Add the two numbers
print("The sum of", num1, "and", num2, "is:", result)  # Print the result

# Output formatting using f-strings 
print(f"The sum of {num1} and {num2} is: {result}")

# A more concise way to take multiple inputs as a list
values = input("Enter two numbers separated by a space: ").split() # Prompt the user for two numbers separated by a space
if len(values) == 2: # Check that the user entered two values
    num1, num2 = map(float, values) # Convert the input values to floats
    result = num1 + num2 # Add the two numbers
    print(f"The sum of {num1} and {num2} is: {result}") 
else: # The user did not enter two values
    print("Please enter two numbers separated by a space.")

#lets find your age using datetime module
from datetime import date # Import the date class from the datetime module
today = date.today() # Get today's date
birth_year = int(input("Enter your birth year: ")) # Prompt the user for their birth year
age = today.year - birth_year # Calculate the user's age
print(f"You are {age} years old.") # Print the user's age

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")
    