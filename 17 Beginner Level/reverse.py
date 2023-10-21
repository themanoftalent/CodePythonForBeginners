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
aStr = "drah reh skcuf fika"
thisislist = []

thisislist.extend(aStr)
print (''.join(thisislist))



size = len(thisislist)
print(size)
for i in range(0,int(size/2)):

    thisislist[i], thisislist[size-1-i] = thisislist[size -1-i], thisislist[i]
print(''.join(thisislist).capitalize(),end='.\n')

