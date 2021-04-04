height = eval(input('Enter height of the modular rectangle: '))
width = eval(input('Enter width of the modular rectangle: '))

count = 0
for i in range(height):
	for j in range(width):
		print(count % 10, end=' ')
		count = count + 1
	print()