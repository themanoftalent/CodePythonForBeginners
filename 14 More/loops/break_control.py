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

# For loop
for s in "test string":
    if s == 's':
        break  # If 's' is encountered, the loop breaks
    print(s, end=" ")
else:
    print("else block")  # This won't be executed because the loop encountered a 'break' statement
print("normal flow")

# While loop
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        break  # If 'a' is even, the loop breaks
    print(a)
else:
    print("else block")  # This won't be executed because the loop encountered a 'break' statement
print("normal flow")
