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
def simpleGeneratorFun(n):

    while n<20:
        yield (n)
        n=n+1
    # return [1,2,3]

x = simpleGeneratorFun(1)
while True:
    try:
        val = next(x) 
        print(val)
        if val == 20:
            break
    except StopIteration as e:
        print(e)
        break



# At each iteration you're advancing the iterator 3 times by making
#  calls to x.__next(). There are usually better patterns in python
# where you don't need to make calls to next directly. For example,
# if you have finite iterator, use a for loop to automatically breaks
#  on StopIteration:
#
# x = simpleGeneratorFun(1)
# for i in x:
#     print i
