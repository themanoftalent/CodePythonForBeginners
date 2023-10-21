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

from contextlib import contextmanager

#it does the same job

@contextmanager
def open_file(filename,mode):
	f.open(filename, mode)
	yield f
	f.close()

with open('context.txt', 'w') as f:
	f.writelines('we are trying but it does the same job')

print(f.close())




#########################################

# class open_file():
#  	def __init__(self, filename,mode):
#  		self.filename = filename
#  		self.mode = mode

#  	def __enter__(self):
#  		self.file=open(self.filename,self.mode)
#  		return self.file


#  	def __exit__(self):
#  		self.file.close()


# with open('context.txt', 'w') as f:
# 	f.writelines('Testing all data on audit')

# print(f.close())


	
