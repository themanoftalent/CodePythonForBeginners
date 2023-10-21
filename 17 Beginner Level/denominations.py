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

def change_possibilities_top_down(amount_left, denominations, current_index=0,coins=[]):
    print "coins: ",coins

    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0: return coins

    # we overshot the amount left (used too many coins)
    if amount_left < 0: return []

    # we're out of denominations
    if current_index == len(denominations): return []

    print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])

    # choose a current coin
    current_coin = denominations[current_index]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    results = []
    while amount_left > 0:
        amount_left -= current_coin
        coins += [current_coin]
        results += change_possibilities_top_down(amount_left, denominations, current_index + 1, coins)
    if amount_left <0:
        return []
    else:
        return results


amount_left = 4
denominations = [2,3]
print change_possibilities_top_down(amount_left, denominations)
