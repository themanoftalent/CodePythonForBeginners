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

#input from the user
def miles2KM():
    miles = float(input("Enter a distance in miles: "))
    conv_fac = 1.609 #conversion factor
#calculating how many kilometers
    kilometers = miles * conv_fac
    #return kilometers
    print("The distance in kilometers is: ",kilometers)

miles2KM()