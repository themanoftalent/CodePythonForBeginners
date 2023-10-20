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
def reverse(alist):

   #intializing pointers
   left = 0
   right = len(alist)-1

   #condition for termination
   while left<right:

       #swapping
       temp = alist[left]
       alist[left] = alist[right]
       alist[right] = temp

       #updating pointers
       left += 1
       right -= 1

   return alist

print(reverse([1,2,3,4,5]))

 