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
def find_rotation_point(words):

    first_word = words[0]

    floor_index = 0
    ceiling_index = len(words)-1
    while floor_index < ceiling_index:
        guess_index = floor_index+((ceiling_index - floor_index)/2)

        if words[guess_index] >= first_word:
            floor_index = guess_index
