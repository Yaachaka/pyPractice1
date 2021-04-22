number = eval(input('Enter a number: '))

print('The divisors: ')
for i in range(1, number):
	if number % i == 0:
		print(i, end='   ')