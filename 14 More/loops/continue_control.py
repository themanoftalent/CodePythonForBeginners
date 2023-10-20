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
    if s == "s":
        continue  # Skip the iteration if 's' is encountered
    print(s, end=' ')

# While loop
a = 0
while a < 10:
    a += 1
    if a % 2 == 1:
        continue  # Skip the iteration if 'a' is odd
    print(a, end=' ')
