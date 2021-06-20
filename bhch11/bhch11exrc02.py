"""
bhch11exrc02.py: Using the dictionary created in the previous problem, allow the user to enter a dollar amount and print out all the products whose price is less than that amount.
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
	
	if item not in item_list:
		price = eval(input('Enter price: '))
		item_list[item] = price
	else:
		print('Item already exists.')

#Give data to user
amt = eval(input('\nEnter amount to list the items whose prices are less than entered amount: '))
l = len(str(int(amt)))
print('{:10s}{:}'.format('Item', 'Price'))
for i in item_list:
	if item_list[i] < amt:
		print('{:10s}${:{:}.2f}'.format(i, item_list[i], l+4))


print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter items and their prices.
To stop type '###' and press 'Enter'.
Item name: Pens
Enter price: 23.32
Item name: computer
Enter price: 234.21
Item name: guitar
Enter price: 123.21
Item name: pens
Item already exists.
Item name: pipe
Enter price: 80.34
Item name: ink
Enter price: 3.32
Item name: ###

Enter amount to list the items whose prices are less than entered amount: 150.00
Item      Price
pens      $  23.32
guitar    $ 123.21
pipe      $  80.34
ink       $   3.32
********************************************************************************
"""