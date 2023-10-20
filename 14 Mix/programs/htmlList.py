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
# def html_list(list_items):
#     HTML_string = "<ul>\\n"
#     for item in list_items:
#         HTML_string += "<li>{}</li>\\n".format(item)
#     HTML_string += "</ul>"
#     return HTML_string
#

#starbox

def starbox(height, width):
    height=6
    width=6
    print('*'*width)
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")
    print ('*' * width)

starbox(13,12)