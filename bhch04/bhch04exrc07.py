print('Enter two numbers: ')
num1 = eval(input())
num2 = eval(input())

if abs(num1 - num2) <= 0.001:
	print('Close')
else:
	print('Not close')