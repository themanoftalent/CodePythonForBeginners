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
def hours2days(input_hours):  # one parameter
    days = input_hours // 24  # divide to 24 withut remainder
    hours = input_hours % 24  # the remainder is 24
    return days, hours


day = hours2days (24)
hour = hours2days (25)
mors = hours2days (10000)

print (day)
print (hour)
print (mors)
