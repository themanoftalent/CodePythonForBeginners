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

tel = {'jack': 4098, 'sape': 4139}
name = {
    4098: 'jack',
    4139: 'sape',
    'abc': 123
}

for line in tel:
    print(line)

print (tel['jack'])
print (name['abc'])

list = ['apple', 'orange']

print (4098 in name)
print ('apple' in list)
print( 0 in list)
