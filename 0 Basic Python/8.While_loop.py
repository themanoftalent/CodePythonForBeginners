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



# Initialize the sum to 0
sum = 0

# Start an infinite loop
while True:
    # Get the input from the user
    number = int(input("Enter a number: "))

    # If the number is 0, break the loop
    if number == 0:
        break

    # Add the number to the sum
    sum += number
    
# Print the sum
print("The sum is", sum)