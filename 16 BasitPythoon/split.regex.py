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

# Split the following irregular sentence into words
import re
sentence = """A, very   very; irregular_sentence."""
#desired_output = "A very very irregular sentence"
#print(re.split('[;,_ \s]+',sentence))
print('\n')
print(" ".join(re.split('[;,._ \s]+', sentence)))

#print(re.sub('\s+',' ',sentence)) ayrica extra whitespace bu sekilde de yok edilebilir

#print(" ".join(re.split('[;,_ s]+', sentence))) #bu haliyle 's' harfini cumleden siler
