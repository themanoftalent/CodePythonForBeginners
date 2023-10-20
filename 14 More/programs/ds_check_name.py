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

def nameAlexSema(Aname, Sname):
    name = input ('What is your name ? ')
    return name


check = nameAlexSema ('Alex', 'Sema')
#print ('your name is ' + str (check))


if str (check)=='Alex' or 'Sema':
    print('Hello %s, I know your name' % str(check))
else:
    print(' The name you input is  '+ str(check))

