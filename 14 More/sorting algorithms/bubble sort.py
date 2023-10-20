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
def myBubble(listem):

	for a in range(len(listem)-1,0,-1):
		for b in range(a):
			if listem[b]>listem[b+1]:
				temp=listem[b]
				listem[b]=listem[b+1]
				listem[b+1]=temp



listem=[1,4,5,2,7,9,6,13,-1]
myBubble(listem)
print(listem)





