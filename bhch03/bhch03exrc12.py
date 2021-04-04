number = eval(input('Enter an integer: '))

fact = 1

for i in range(number, 1, -1):
	fact = fact*i

print('Factorial of the given number:', fact)