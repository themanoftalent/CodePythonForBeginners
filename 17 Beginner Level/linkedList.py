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
class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.cur_node = None
    def add(self, data):
        new_node = node(data)
        new_node.next = self.cur_node
        self.cur_node = new_node
    def printlist(self):
        node = self.cur_node
        while node:
            print node.value
            node = node.next
        
         
        
mylist = linkedList()
mylist.add(3)
mylist.add(2)
mylist.add(23)
mylist.printlist()
