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
# # Declare a variable and initialize it
# f = 101
# print (f)
#
#
# # Global vs. local variables in functions
# def someFunction():
#     global f
#     f = 'I am learning Python'
#     # print (f)
#
#
# someFunction ()
# print (f)

print ('==' * 14)

fa = 102
print (fa)


# Global vs.local variables in functions
def somedFunction():
    global fa


print (fa)
fa = "changing global variable"

somedFunction ()
print (fa)
