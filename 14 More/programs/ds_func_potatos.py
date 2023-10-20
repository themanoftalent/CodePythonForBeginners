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

def potatoCost(price, amount, Ptype):
    cost=price*amount
    print(Ptype)
    print(cost)
    print(amount)
    return cost, Ptype, price

potatoCost(10,5,3.4)