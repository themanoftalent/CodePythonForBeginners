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

#factorial
def factorial(n):
    '''We are writinga factorial source code example'''
    if n==0:
        return 1
    else:
        return n*factorial(n-1)



print(factorial(5))


#lets write a palindrome
def palin(word):
    '''We are writiting a palindrome for better'''
    if len(word)<1:
        return True
    elif word[0]==word[-1]:
        return palin(word[1:-1])

    else:
        return False


print(palin('mum'))