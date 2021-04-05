from random import randint

guess = eval(input('Guess a number between 1 and 10: '))

if 0 < guess < 11:
	rand = randint(1, 10)
	if rand == guess:
		print('Woww.. you guessed it right.')
	else:
		print('Alas... The random number generated is', rand)
else:
	print('Out of bound guess.')