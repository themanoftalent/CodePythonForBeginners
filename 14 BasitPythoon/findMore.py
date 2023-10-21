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
import re

texted="""
"Roses Are Red" can refer to a specific poem, or a class of poems inspired by that poem. 
It has a Roud Folk Song Index number of 19798. It is most commonly used as a love poem. 
Roses are red, Violets are blue, Sugar is sweet, And so are you."""


finding=r'r\w+'

result=re.findall(finding,texted,flags=re.I)

print(result)

#################################################

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print ('Found "%s" in "%s" from %d to %d ("%s")' % (match.re.pattern, match.string, s, e, text[s:e]))
