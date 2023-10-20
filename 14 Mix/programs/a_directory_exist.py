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

import os.path
from os import path

def main():
   print('Os Path is ', os.path)
   print ("file exist:"+str(path.exists('guru99.txt')))
   print ("File exists:" + str(path.exists('career.guru99.txt')))
   print ("directory exists:" + str(path.exists('myDirectory')))
   print('File exists',str(path.exists("Dosya.txt")))
   print('Dosya bulunmakta '+str(path.exists("Patasana.text")))
   print('Dosya var ', str(path.exists('Puslu Ada')))
   print("**"*20)
   print ("Is it Directory? " + str (path.isdir ('guru99.txt')))
   print ("Is it Directory? " + str (path.isdir ('myDirectory')))

if __name__== "__main__":
   main()