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

import os
import os.path
import sys

# Your path here e.g. "C:\Program Files\text.txt"
# For access purposes: "C:\\Program Files\\text.txt"
#for macos path.expanduser()

normalPath=os.path.expanduser('~/Desktop/Salma')

if os.path.exists(normalPath):
    print ("File found!")
else:
    print ("File not found!")
print('===================')




print('Where the file is locaated: ',os.getcwd())

print(help(os.path))
print('*************************')
print(os.path.dirname('Users/darwin/Desktop'))
print(os.environ)
print('==========NORMAL======')
print()
print(os.listdir())


