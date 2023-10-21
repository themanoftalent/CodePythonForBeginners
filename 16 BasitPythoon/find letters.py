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

yazi=""" Aleda ava giderken avdan gelen Abiye abla nerde demis 
avci avdan uzak Ahmet amca kulubeye gitmis, ale,aleda buyumek cok guzel,no 
alemdar, adanada yolda asya kitasinda aglamis sanirim. ablanda alba
"""
print('Toplamda kullanilan karakter sayisi',len(yazi))

buda_text=r'\bA\w+'
buda_iki=r'b\w+'
buda_uc=r'[\w+]' #all chars


sonuc=re.findall(buda_text,yazi,flags=re.I)
print(sonuc,len(sonuc),'a harfi bulunmakta.')
print()

sonuc2=re.findall(buda_iki,yazi,flags=re.I)
print(sonuc2,len(sonuc2),'b harfi bulunmakta.')
print()

sonuc3=re.findall(buda_uc,yazi,flags=re.I)
print(sonuc3,len(sonuc3),'karekter bulunmakta')



