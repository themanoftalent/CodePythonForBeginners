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
# Python code to demonstrate working of
# heapify(), heappush() and heappop() 

# importing "heapq" to implement heap queue 
import heapq 

# initializing list 
li = [5, 7, 9, 1, 3] 

# using heapify to convert list into heap 
heapq.heapify(li) 

# printing created heap 
print ("The created heap is : ",end="") 
print (list(li)) 

# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(li,4) 

# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(li)) 

# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 
