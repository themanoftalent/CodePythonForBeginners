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
class Calculator: 
	'''Lets make a simple calculator'''



	def __init__(self):
		self.curValue = 0

	def __repr__(self):
		return "my Calculator"

	def subtract(self, number):
		self.curValue -= number

	def add(self, number):
		self.curValue += number


mycalc = Calculator()
mycalc.add(12)
mycalc.subtract(10)
print (mycalc.curValue)
print('###############')
print (mycalc) #when we print out function it returns a repr srting

