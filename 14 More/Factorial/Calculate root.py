import math
try:
	number=int(input('Enter a number'))
except IOError:
	print('Wrong input')
	if number<0:
		print('Negative number')
except ZeroDivision:
	print('Try again zero division')
finally:
	print('The square of {} is {:}'.format(number, math.sqrt(number)))