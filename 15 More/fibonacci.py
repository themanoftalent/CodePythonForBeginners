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
#get nth value in fibonacci sequence
class Fib:
    def __init__(self):
        self.saved_vals = {}

    def get_nth(self, n):
        if n in [0, 1]:
            return n
        if n in self.saved_vals:
            return self.saved_vals[n]
        else:
            result = self.get_nth(n - 1) + self.get_nth(n - 2)
            self.saved_vals[n] = result
            return result

my_fib = Fib()
print(my_fib.get_nth(90))
