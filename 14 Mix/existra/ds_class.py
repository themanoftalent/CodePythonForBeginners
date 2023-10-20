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

class merhaba:

    def login(self, kadi):
        kadi = (int (input ('Enter a password')))
        while kadi != 123:
            break

    def selam(self, isim, yas, memleket):
        self.isim = isim
        self.yas = yas
        self.memleket = memleket
        print (isim, yas, memleket)


kadi = merhaba ()
while kadi==123:
    continue
kadi.login (kadi)

kadi.selam ('Ahmet', 24, 'istanbul')
