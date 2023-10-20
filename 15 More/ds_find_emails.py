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

import re
mailAddress='guru99@google.com, careerguru99@hotmail.com , users@yahoomail.com'

emails=re.findall(r'[\w\.-]+@[\w\.-]+',mailAddress)

print('Printing all emails')
for mail in emails:
    print(emails)