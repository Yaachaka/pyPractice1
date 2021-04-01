height = eval(input('Enter the height of the diamond: '))

j = 1
for i in range(height//2, 0, -1):
	print(' ' * i, '*' * (2*j-1), sep = '')
	j = j + 1

print('*' * height)

j = height//2
for i in range(1, height//2 + 1):
	print(' ' * i, '*' * (2*j-1), sep = '')
	j = j-1