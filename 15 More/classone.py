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

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name

        if self.name != " ":
            Student.count += 1
        else:
            Student.count = Student.count #indent
