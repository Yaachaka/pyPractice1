"""
@@@@ Program statement:
In the last chapter there was an exercise that asked you to create 
a multiplication game for kids. Improve your program from that 
exercise to keep track of the number of right and wrong answers. 
At the end of the program, print a message that varies depending on how
many questions the player got right.
"""
from random import randint

right = 0
wrong = 0
for i in range(10):
	num1 = randint(1, 10)
	num2 = randint(1, 10)
	
	print('Question', i+1, ':', num1, 'x', num2, '=', end=' ')
	answer = eval(input())
	if answer == num1 * num2:
		print('Right!')
		right = right + 1
	else:
		print('Wrong. The answer is', num1 * num2)
		wrong = wrong + 1

print()
print('No. of right answers:', right)
print('No. of wrong answers:', wrong)