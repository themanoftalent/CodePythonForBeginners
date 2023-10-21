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
    y=input("Enter year to be checked:")
    try:

        if(int(y)%4==0 and int(y)%100!=0 or int(y)%400==0):
            print("This year is a leap year!")
        else:
            print("This year is not a leap year!")
    except:
        print("Invalid entry")
if __name__ == '__main__':
    main()
