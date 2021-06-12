"""
bhch09exrc06.py: Modify the higher/lower program so that when there is only one guess left, it says 1 guess, not 1 guesses.
"""
print('*'*80)

from random import randint

secret_num = randint(1,100)
num_guesses = 0
guess = 0
while guess != secret_num and num_guesses <= 4:
	guess = eval(input('Enter your guess (1-100): '))
	num_guesses = num_guesses + 1

	str1 = 'guesses'
	if 5-num_guesses == 1:
		str1 = str1[:-2]

	if guess < secret_num:
		print('HIGHER.', 5-num_guesses, str1, 'left.\n')
	elif guess > secret_num:
		print('LOWER.', 5-num_guesses, str1, 'left.\n')
	else:
		print('You got it!')
if num_guesses==5 and guess != secret_num:
	print('You lose. The correct number is', secret_num)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter your guess (1-100): 56
LOWER. 4 guesses left.

Enter your guess (1-100): 30
HIGHER. 3 guesses left.

Enter your guess (1-100): 45
LOWER. 2 guesses left.

Enter your guess (1-100): 38
You got it!
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter your guess (1-100): 56
HIGHER. 4 guesses left.

Enter your guess (1-100): 45
HIGHER. 3 guesses left.

Enter your guess (1-100): 78
HIGHER. 2 guesses left.

Enter your guess (1-100): 89
HIGHER. 1 guess left.

Enter your guess (1-100): 90
You got it!
********************************************************************************
"""