def kwar_func(tekDeger,**cokDegerler):
	print(f"a'nin degeri {tekDeger}") 
	#format yerine f string kullandik
	print()
	


	for sayi,sira in enumerate(cokDegerler.items(),start=1):
		print('{} :{}'.format(sayi,sira))
		

	



print(kwar_func(45,akif=5600,Hakan=3400,Ismail=4100,Muhsin=5500,Mehmet=3100,Humeyra=3110,Kubilay=5100))