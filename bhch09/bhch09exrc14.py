"""
bhch09exrc14.py: Write a program to play the following simple game. The player starts with $100. On each turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each correct guess and loses $10 for each incorrect guess. The game ends either when the player runs out of money or gets to $200.
"""
print('*'*80)

from random import randint

mat = 100

while True:
	guess = eval(input('Your guess?(1-heads, 2-tails): '))
	toss = randint(1, 2)
	if guess == toss:
		mat = mat + 9
		print('You win.. You hold $', mat)
	else:
		mat = mat - 10
		print('You lose.. You hold $', mat)
	
	if mat <= 0 or mat >= 200:
		print('You are empty handed. Goodbye...')
		break
	if mat >= 200:
		print('Your current possession is $', mat, '. Farewell...', sep='')
		break

print('*'*80)
"""PROGRAM OUTPUT
*******************************************************************************
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 90
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 99
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 108
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 117
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 126
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 116
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 125
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 134
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 124
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 133
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 123
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 113
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 103
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 93
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 83
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 92
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 101
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 91
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 81
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 71
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 80
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 70
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 79
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 88
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 97
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 87
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 96
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 86
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 76
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 85
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 94
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 84
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 74
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 83
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 73
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 63
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 72
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 81
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 90
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 80
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 70
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 79
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 69
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 59
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 68
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 58
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 67
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 57
Your guess?(1-heads, 2-tails): 2
You win.. You hold $ 66
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 75
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 65
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 74
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ 64
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 54
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 44
Your guess?(1-heads, 2-tails): 1
You win.. You hold $ 53
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 43
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 33
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 23
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 13
Your guess?(1-heads, 2-tails): 1
You lose.. You hold $ 3
Your guess?(1-heads, 2-tails): 2
You lose.. You hold $ -7
You are empty handed. Goodbye...
********************************************************************************
"""