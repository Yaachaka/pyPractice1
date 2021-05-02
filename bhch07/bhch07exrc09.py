"""
bhch07exrc09.py: 
When playing games where you have to roll two dice, it is nice to know the odds of each roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about 17%. You can compute these mathematically, but if you don’t know the math, you can write a program to do it. To do this, your program should simulate rolling two dice about 10,000 times and compute and print out the percentage of rolls that come out to be 2, 3, 4, ..., 12.
"""
print('*'*80)
from random import randint

rolls = [0] * 11
odds = []

ntrials = 20
for i in range(ntrials):
	dice1 = randint(1, 6)
	dice2 = randint(1, 6)
	position = dice1 + dice2 - 2
	rolls[position] = rolls[position] + 1

for i in range(len(rolls)):
	odds.append(100 * rolls[i] / ntrials)

print('[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]\t: Dice values')
print(rolls, '\t: No of times appeared out of', ntrials, 'trials')
print(odds, '\t: Odds of rolling each value (%).')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]    : Dice values
[0, 2, 1, 1, 3, 4, 3, 3, 1, 0, 2]       : No of times appeared out of 20 trials
[0.0, 10.0, 5.0, 5.0, 15.0, 20.0, 15.0, 15.0, 5.0, 0.0, 10.0]   : Odds of rolling each value (%).
********************************************************************************

@@@@ Trial2:
********************************************************************************
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]    : Dice values
[1, 1, 2, 1, 3, 4, 2, 1, 3, 2, 0]       : No of times appeared out of 20 trials
[5.0, 5.0, 10.0, 5.0, 15.0, 20.0, 10.0, 5.0, 15.0, 10.0, 0.0]   : Odds of rolling each value (%).
********************************************************************************

@@@@ Trial3:
********************************************************************************
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]    : Dice values
[0, 3, 2, 1, 1, 5, 5, 2, 0, 0, 1]       : No of times appeared out of 20 trials
[0.0, 15.0, 10.0, 5.0, 5.0, 25.0, 25.0, 10.0, 0.0, 0.0, 5.0]    : Odds of rolling each value (%).
********************************************************************************
"""