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


from subclass_exercise import *

dash = Pet("dash", "horse")
pongo = Dog("pongo", True)
furry = Cat("furry", True)

print( "Horse: %s" % dash)
print( "Dog: %s" % pongo)
print( "Cat: %s" % furry)


print( "furry is an instance of Pet: %r" % isinstance(furry, Pet))
print( "furry is an instance of Cat: %r" % isinstance(furry, Cat))
print( "pongo is an instance of Pet: %r" % isinstance(pongo, Pet))
print( "dash is an instance of Pet: %r" % isinstance(dash, Pet))
print( "pongo is an instance of Cat: %r" % isinstance(pongo, Cat))
print( "dash is an instance of Dog: %r" % isinstance(dash, Dog))
