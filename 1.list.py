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


#This is a list in python
#List is a collection of items in a particular order

bicycles = ['trek','cannondale','redline','specialized']  #This is a list of bicycles
print(bicycles) #This will print the list of bicycles
print("\n") #This will print a new line
print(bicycles[0]) #This will print the first element of the list
print("\n") #This will print a new line
print(bicycles[0].title()) #This will print the first element of the list
print("\n") #This will print a new line
print(bicycles[1]) #This will print the second element of the list
print("\n") #This will print a new line
print(bicycles[3]) #This will print the fourth element of the list
print("\n") #This will print a new line
#now lets add to the list
bicycles.append('ducati') #This will add ducati to the list
print(bicycles) #This will print the list of bicycles
print("\n") #This will print a new line
#now lets add to the list
bicycles.insert(0,'carrera') #This will add carrera to the list
print(bicycles) #This will print the list of bicycles
print("\n") #This will print a new line
#now lets remove from the list
del bicycles[0] #This will remove carrera from the list
print(bicycles) #This will print the list of bicycles
print("\n") #This will print a new line
#now lets remove from the list
del bicycles[1] #This will remove cannondale from the list
print(bicycles) #This will print the list of bicycles
print("\n") #This will print a new line
#now lets remove from the list
del bicycles[2] #This will remove specialized from the list
print(bicycles) #This will print the list of bicycles
print("\n") #This will print a new line
# lets add a list to the list of bicycles
motorcycles = ['honda','yamaha','suzuki'] #This is a list of motorcycles
print(motorcycles) #This will print the list of motorcycles
print("\n") #This will print a new line
# lets add a list to the list of bicycles
newlist = bicycles + motorcycles #This will add the list of bicycles to the list of motorcycles
print(newlist) #This will print the new list
