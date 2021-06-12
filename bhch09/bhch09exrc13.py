"""
bhch09exrc13.py: In Chapter 4 there was a problem that asked you to write a program that lets the user play Rock-Paper-Scissors against the computer. In that program there were exactly five rounds. Rewrite the program so that it is a best 3 out of 5. That is, the first player to win three times is the winner.
"""
print('*'*80)

from random import randint

won = 0
lose = 0
ties = 0

i = 0
while True:
	print('Round', i+1, ':')
	i = i+1
	sys_choice = randint(1, 3)
	your_choice = eval(input('what is your choice?(1-rock, 2-paper, 3-scissor): '))
	print(' '*5, 'Systems choice:', sys_choice)
	if sys_choice == your_choice:
		ties = ties + 1
	elif (sys_choice == 1) and (your_choice == 2):
		won = won + 1
	elif (sys_choice == 1) and (your_choice == 3):
		lose = lose + 1
	elif (sys_choice == 2) and (your_choice == 1):
		lose = lose + 1
	elif (sys_choice == 2) and (your_choice == 3):
		won = won + 1
	elif (sys_choice == 3) and (your_choice == 1):
		won = won + 1
	else:
		lose = lose + 1
	if won == 3 or lose == 3:
		break

print('')
print('Result:')
if won == 3:
	print('You win. Computer loses.')
if lose == 3:
	print('Computer wins.')
print('Wins:', won)
print('Lost:', lose)
print('Ties:', ties)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Round 1 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 2
Round 2 :
what is your choice?(1-rock, 2-paper, 3-scissor): 3
      Systems choice: 1
Round 3 :
what is your choice?(1-rock, 2-paper, 3-scissor): 1
      Systems choice: 1
Round 4 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 2
Round 5 :
what is your choice?(1-rock, 2-paper, 3-scissor): 3
      Systems choice: 1
Round 6 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 1
Round 7 :
what is your choice?(1-rock, 2-paper, 3-scissor): 1
      Systems choice: 3
Round 8 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 3

Result:
Computer wins.
Wins: 2
Lost: 3
Ties: 3
********************************************************************************

@@@@ Trial2:
********************************************************************************
Round 1 :
what is your choice?(1-rock, 2-paper, 3-scissor): 3
      Systems choice: 1
Round 2 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 2
Round 3 :
what is your choice?(1-rock, 2-paper, 3-scissor): 1
      Systems choice: 3
Round 4 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 1
Round 5 :
what is your choice?(1-rock, 2-paper, 3-scissor): 3
      Systems choice: 1
Round 6 :
what is your choice?(1-rock, 2-paper, 3-scissor): 1
      Systems choice: 1
Round 7 :
what is your choice?(1-rock, 2-paper, 3-scissor): 2
      Systems choice: 1

Result:
You win. Computer loses.
Wins: 3
Lost: 2
Ties: 2
********************************************************************************
"""