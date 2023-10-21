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
#there is one duplicate in a range of number, find the duplicate
#O(n) time 
mylist = [1,2,3,4]
def find_repeat(numbers):
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            return numbers[i]
    return None

print(find_repeat(mylist))
