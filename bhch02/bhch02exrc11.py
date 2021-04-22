height = eval(input('Enter height of the box: '))
width = eval(input('Enter widt of the box: '))

print('*'*width)
for i in range(height - 2):
	print('*', ' '*(width-2), '*', sep = '')
print('*'*width)
