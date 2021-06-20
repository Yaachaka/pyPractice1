"""
bhch11exrc01.py: Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys are the product names and whose values are the prices. When the user is done entering products and prices, allow them to repeatedly enter a product name and print the corresponding price or a message if the product is not in the dictionary.
"""
print('*'*80)

print('Enter items and their prices.')
print('To stop type \'###\' and press \'Enter\'.')

item_list = {}
#Get data from user
while True:
	item = input('Item name: ').lower()
	if item == '###':#To stop recieving input
		break
	price = eval(input('Enter price: '))
	if item not in item_list:
		item_list[item] = price
	else:
		print('Item already exists.')

#Give data to user
print('\nEnter item name to know its price.')
print('To stop type \'###\' and press \'Enter\'.')
while True:
	item = input('Item name: ').lower()
	if item == '###':#To stop information exchange
		break
	if item in item_list:
		print('Price: ${:}'.format(item_list[item]))
	else:
		print('Item does not exist.')


print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter items and their prices.
To stop type '###' and press 'Enter'.
Item name: Pens
Enter price: 23.45
Item name: pencil
Enter price: 56.45
Item name: ink
Enter price: 3.32
Item name: ###

Enter item name to know its price.
To stop type '###' and press 'Enter'.
Item name: ink
Price: $3.32
Item name: book
Item does not exist.
Item name: ###
********************************************************************************
"""