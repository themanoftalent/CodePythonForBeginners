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
import datetime
import calendar

today=datetime.date.today()
print('Simdiki tarih ',today)
print('###############')

days_in_current_month=calendar.monthrange(today.year,today.month)[1] #bunda [1] olmadan hata veriyor
print('Subat ayi ',days_in_current_month)

print('###############')
days_left= days_in_current_month - today.day
print(days_left)

print('###############')
print('Lets find the start day for the next month')
start_date=today+datetime.timedelta(days=days_left+1)
print(start_date)
