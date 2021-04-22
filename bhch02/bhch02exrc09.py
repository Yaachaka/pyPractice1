count = eval(input('How many fibonacci numbers do you want to print?: '))

a = 0
b = 1

print(a, end = '')
for i in range(count-1):
	print(', ', b, end = '')
	temp = a
	a = b
	b = temp + b