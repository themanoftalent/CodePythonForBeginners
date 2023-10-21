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
#Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

import re


text = """
Betty bought a bit of butter, But the butter was so bitter, 
So she bought some better butter, To make the bitter butter better.
"""

my_pattern = r'\bB\w+'  #b boundry sinir

print(re.findall(my_pattern,text,flags=re.IGNORECASE))
