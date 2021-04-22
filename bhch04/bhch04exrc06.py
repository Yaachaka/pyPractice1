n_items = eval(input('Enter number of items: '))

if n_items < 10:
	print('The total cost is', n_items * 12)
elif n_items <100:
	print('The total cost is', n_items * 10)
else:
	print('The total cost is', n_items * 7)