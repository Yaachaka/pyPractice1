from random import randint

for i in range(10):
	num1 = randint(1, 10)
	num2 = randint(1, 10)
	
	print('Question', i+1, ':', num1, 'x', num2, '=', end=' ')
	answer = eval(input())
	if answer == num1 * num2:
		print('Right!')
	else:
		print('Wrong. The answer is', num1 * num2)