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


# *args allows you to pass a variable number of positional arguments to a function.
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# Call the function with different numbers of arguments
sum1 = add(2, 3)
sum2 = add(1, 4, 5, 6)

print(sum1)  # Output: 5
print(sum2)  # Output: 16
