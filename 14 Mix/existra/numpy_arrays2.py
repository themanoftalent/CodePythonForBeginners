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

look = [12.2, 34.32, 34.5, 198.54, 56, 44, 321, 789, 654, 90]

import numpy as np

np_look = np.array (look)

# now we create lbs
np_look_lbs = np_look // 4 ** 2

print (np_look_lbs)
