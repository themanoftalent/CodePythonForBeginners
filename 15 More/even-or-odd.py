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
def main():
    a=input("enter a number=")
    try:
     x=int(a)%2
     if(int(x)==0):
        print(a+" is even")
     else:
        print(a+" is odd")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
