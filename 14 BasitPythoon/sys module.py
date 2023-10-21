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
import sys
import path

my_file_path=path
print('Shows where my file is located')
print(my_file_path)


print('')

for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
