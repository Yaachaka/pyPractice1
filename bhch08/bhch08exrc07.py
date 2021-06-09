"""
bhch08exrc07.py: Write a program that estimates the average number of drawings it takes before the user’s numbers are picked in a lottery that consists of correctly picking six different numbers that are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of user numbers and simulates drawings until the user’s numbers are drawn. Find the average number of drawings needed over the 1000 times the loop runs.
"""
print('*'*80)

from random import randint, shuffle, choice

lotteries = [i for i in range(1, 10)]
times = 100
avg = 0

for i in range(times):
	# Player
	choose = randint(1,10)

	# System
	shuffle(lotteries)

	choose2 = choice(lotteries)

	if choose == choose2:
		avg = avg + 1

print('Out of', times, 'trials, the average is', round(times/avg, 4))
print('We got correct lottery', avg, 'times.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Out of 100 trials, the average is 12.5
We got correct lottery 8 times.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Out of 100 trials, the average is 8.3333
We got correct lottery 12 times.
********************************************************************************
"""