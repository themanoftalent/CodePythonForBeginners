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
# import os
# import os.path
# print(os.path.exists("/etc/password.txt"))
# #we have path exist function
#
#
# print (os.path.isfile("/etc/password.txt"))
#
#
# #also
#
# import os
# import os.path
# PATH='./file.txt'
#
# if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
#     print( "File exists and is readable")
# else:
#     print( "Either file is missing or is not readable")

import os
import os.path

PATH = ('/etc/Myfile.txt')

print(os.path.exists('/etc/Myfile.txt'))

if os.path.isfile(PATH):
    print('File found')
else:
    print('Try again')
