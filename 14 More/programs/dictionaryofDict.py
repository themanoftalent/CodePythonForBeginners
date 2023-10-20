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

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

for element in elements:
    print(element)

print('*'*23)

print(elements['hydrogen'])

print(elements.get('helium'))

print(elements.get('unobtainium', 'There\'s no such element!'))

print(elements.get('Akifium', 'No such element '))