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
for i in range(101):

    if not i%3 and not i%5:
        print "FizzBuzz"
    elif not i%3:
            print "Fizz"
    elif not i%5:
            print "Buzz"
    else: 
        print i
