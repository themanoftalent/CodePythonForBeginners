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

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(0, 25, 1):
        print(i, end = ' ')
    print()
    for i in inclusive_range_v2(25):
        print(i, end = ' ')
    print()
    for i in inclusive_range_v2(0, 25):
        print(i, end = ' ')
    print()
    for i in inclusive_range_v2(5, 25):
        print(i, end = ' ')
    print()
    for i in inclusive_range_v2(5, 25,30,40):
        print(i, end = ' ')


# yield() is a key statement for defining a generator
def inclusive_range(start, stop, step = 1):
    i = start
    while i <= stop:
        yield(i)
        i+= step

def inclusive_range_v2(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        start = 0
        stop = args[0]
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError("inclusive_range_v2 expects at most 3 arguments, got {}".format(numargs))
    i = start
    while i <= stop:
        yield(i)
        i+= step

if __name__ == "__main__": main()
