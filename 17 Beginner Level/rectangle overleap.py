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
def check_for_overlap():
    rectangle_a  = {"x1":15, "y1":10, "x2":10,"y2":5}
    rectangle_b  = {"x1": 25, "y1":10, "x2":15,"y2":5}
    #black color                           or    red color
    if(rectangle_a["y1"]<rectangle_b["y2"] or rectangle_a["x1"]<rectangle_b["x2"]):
        print("no overlap ")
    #the blue color                          or   green 
    elif(rectangle_a["x2"]>rectangle_b["x1"] or rectangle_a["y2"]>rectangle_b["y1"]):
        print("no overlap ")
    else:
        print("YES ! there is a overlap")

check_for_overlap()
