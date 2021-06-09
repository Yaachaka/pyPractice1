"""
bhch08exrc06.py: Write a simple lottery drawing program. The lottery drawing should consist of six different numbers between 1 and 48.
"""
print('*'*80)

from random import randint, shuffle, choice

# Player
choose = eval(input('Choose your lottery (between 1 and 48): '))

if choose < 1 or choose > 48:
	choose = 48
	print('You chose 48.')

# System
lotteries = [i for i in range(1, 49)]
shuffle(lotteries)

choose2 = choice(lotteries)

if choose == choose2:
	print('You are lucky.. You win the lottery..')
else:
	print('Unfortunate.. the lucky lottery is', choose2)


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Choose your lottery (between 1 and 48): 32
Unfortunate.. the lucky lottery is 3
********************************************************************************

@@@@ Trial2:
********************************************************************************
Choose your lottery (between 1 and 48): 14
Unfortunate.. the lucky lottery is 1
********************************************************************************

@@@@ Trial3:
********************************************************************************
Choose your lottery (between 1 and 48): 65
You chose 48.
Unfortunate.. the lucky lottery is 7
********************************************************************************
"""