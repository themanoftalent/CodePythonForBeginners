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
import pathlib
import pathlib
#to create a folder
newpath = os.path.expanduser('~/Desktop/bura/folderz')
if not os.path.exists(newpath):
    os.makedirs(newpath)

#to remove a folder
newpath = os.path.expanduser('~/Desktop/bura/myfold')
if os.path.exists(newpath):
    os.removedirs(newpath)
