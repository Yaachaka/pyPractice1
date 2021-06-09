"""
bhch08exrc24.py: The following is useful in implementing computer players in a number of different games. Write a program that creates a 5 x 5 list consisting of zeroes and ones. Your program should then pick a random location in the list that contains a zero and change it to a one. If all the entries are one, the program should say so. [Hint: one way to do this is to create a new list whose items are the coordinates of all the ones in the list and use the choice method to randomly select one. Use a two-element list to represent a set of coordinates.]
"""
print('*'*80)

from random import randint, choice

field = [[randint(0,1) for j in range(5)] for i in range(5)]

print('Before:\nfield:', field)

ones = [[i, j] for i in range(5) for j in range(5) if field[i][j]]
zeroes = [[i, j] for i in range(5) for j in range(5) if not field[i][j]]

count = 0
for i in range(len(zeroes) + 1):
	if len(ones) == 25:
		print('All the entries are one.')
		print('Ran', count, 'times')
		break
	count = count + 1
	coord = zeroes.pop(zeroes.index(choice(zeroes)))
	ones.append(coord)
	field[coord[0]][coord[1]] = 1

print('After:\nfield:', field)


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Before:
field: [[1, 0, 0, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 1]]
All the entries are one.
Ran 16 times
After:
field: [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
********************************************************************************

@@@@ Trial2:
********************************************************************************
Before:
field: [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 1, 0, 1, 0], [0, 1, 0, 1, 0]]
All the entries are one.
Ran 12 times
After:
field: [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
********************************************************************************
"""