credits = eval(input('Enter the number of credits you took: '))

if credits < 24:
	print('The student is freshman.')
elif credits < 54:
	print('The student is sophomore.')
elif credits < 84:
	print('The student is a junior.')
else:
	print('The student is a senior.')