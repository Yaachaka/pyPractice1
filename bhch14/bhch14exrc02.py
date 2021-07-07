"""
bhch14exrc02.py: Write a class called Product. The class should have fields called name, amount, and price, holding the product’s name, the number of items of that product in stock, and the regular price of the product. There should be a method get_price that receives the number of items to be bought and returns a the cost of buying that many items, where the regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should also be a method called make_purchase that receives the number of items to be bought and decreases amount by that much.
"""
print('*'*80)

class Product:
	def __init__(self, name, amount, price):
		self.name = name#Product's name
		self.amount = amount#Number of items
		self.price = price#Regular price of the product
	
	def get_price(self, amount):
		p = amount * price
		if 9 < amount < 100:
			p = 90 * p / 100
		elif amount > 99:
			p = 80 * p / 100
		return p
	def make_purchase(self, amount):
		return self.get_price(amount)

name = input('Enter product name: ')
amount = eval(input('Enter number of items: '))
price = eval(input('Enter price per product: '))
p1 = Product(name, amount, price)

print('The final discount price is ${:}.'.format(p1.get_price(amount)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter product name: tv
Enter number of items: 56
Enter price per product: 45
The final discount price is $2268.0.
********************************************************************************
"""