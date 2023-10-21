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
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
          #'dict' object has no attribute 'sort' so we use a list



points.sort(key=lambda i: i['x'])
print(points)
