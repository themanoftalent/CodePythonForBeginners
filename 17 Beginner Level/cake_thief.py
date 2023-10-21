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
cake_tuples = [(7,160), (3,90), (2,15)]
capacity = 20
import itertools
def max_duffel_bag_value(cake_tuples, capacity):
    #get all possible permutation, then sort to get the max
    allPerms = list(itertools.permutations(cake_tuples))
    for i in allPerms:
        sum = 0
        for cake in i:
            sum += cake[0]
        print (sum)
max_duffel_bag_value(cake_tuples, capacity)
