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
"""
Write a function that takes an integer flight_length (in minutes) and a 
list of integers movie_lengths (in minutes) and returns a boolean indicating 
whether there are two numbers in movie_lengths whose sum equals flight_length.

O(n) time
"""
flight_length = 220
movie_lengths = [120,120]
def findMovie(flight_length, movie_lengths):
    difference = set()
    for i in movie_lengths:
        if i in difference:
            return True
        else:
            difference.add(flight_length-i)
    return False

print findMovie(flight_length, movie_lengths)
