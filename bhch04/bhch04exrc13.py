from random import randint

won = 0
lose = 0
ties = 0

for i in range(5):
	print('Round', i+1, ':')
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

print('')
print('Result:')
print('Wins:', won)
print('Lost:', lose)
print('Ties:', ties)