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
def kwar_func(tekDeger,**cokDegerler):
	print(f"a'nin degeri {tekDeger}") 
	#format yerine f string kullandik
	print()
	


	for sayi,sira in enumerate(cokDegerler.items(),start=1):
		print('{} :{}'.format(sayi,sira))
		

	



print(kwar_func(45,akif=5600,Hakan=3400,Ismail=4100,Muhsin=5500,Mehmet=3100,Humeyra=3110,Kubilay=5100))
