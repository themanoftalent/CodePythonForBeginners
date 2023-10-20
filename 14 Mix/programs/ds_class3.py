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

#!/usr/bin/python

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary


print ("Employee.__doc__:",   Employee.__doc__)
print ("Employee.__name__:",  Employee.__name__)
print ("Employee.__module__:",Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print('\n')
print ("Employee.__dict__:",  Employee.__dict__)
