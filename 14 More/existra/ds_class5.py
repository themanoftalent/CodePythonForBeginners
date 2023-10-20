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

class Animals:
    def __init__(self, name, age, color, weight, height):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
        self.height = height

    def printAll(self):
        print(self.name, self.age, self.color, self.weight, self.height)

    def printName(self):
        print(self.name)

    def printAge(self):
        print(self.age)

    def printColor(self):
        print(self.color)


    def printWeight(self):
        print(self.weight)

    def printHeight(self):
        print(self.height)

    def printAll(self):
        print(self.name, self.age, self.color, self.weight, self.height)


# main program
animal1 = Animals('dog', 5, 'black', 20, 50)
animal2 = Animals('cat', 3, 'white', 10, 30)
animal3 = Animals('bird', 1, 'yellow', 1, 10)
animal4 = Animals('fish', 2, 'blue', 0.5, 5)

animal1.printAll()
animal2.printAll()
animal3.printAll()
animal4.printAll()

animal1.printName()
animal2.printName()
animal3.printName()
animal4.printName()
