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
myseq = [["ab"], "b", [["c", "d"], "e",],"f"]
def getList(seq):
    newstring = ""
    for i in seq:
        if type(i) is str:
            newstring += i
        else:
            newstring += getList(i)
    return newstring
print getList(myseq)
