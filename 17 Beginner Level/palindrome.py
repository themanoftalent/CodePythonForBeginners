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
def palindromes(text):
    text = text.lower()
    results = []
    for i in range(len(text)):
        for j in range(i):
            chunk = text[j:i+1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    if len(sorted(results,key=len)) == 0:
        return text[0]
    else:
        return sorted(results, key=len)
mystring = raw_input("Please entere a word and I will find the longest palindrome:\n")
print palindromes(mystring)
