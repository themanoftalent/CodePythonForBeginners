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
f = open("straight_linez.txt","r")
#first line is useless
f.readline()

x = []
y = []
z = []

for line in f:
    line = line.replace("\n","").replace("\t"," ").split(" ")
    x.append(line[0])
    y.append(line[0])
    z.append(line[2])
print (float(max(z))// float(min(z)))

