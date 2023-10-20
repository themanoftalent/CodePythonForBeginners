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

def garden_calendar(season):
    if season == "spring":
        print ("time to plant the garden!")
    elif season == "summer":
        print ("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print ("time to harvest the garden!")
    elif season == "winter":
        print ("time to stay indoors and drink tea!")
    else:
        print ("I don't recognize that season")


#garden_calendar("spring") #we have to call the function
garden_calendar(input("Enter your favorite season :"))

