"""
bhch10exrc29.py: The following is useful as part of a program to play Minesweeper. Suppose you have a 5 x 5 list that consists of zeros and M’s. Write a program that creates a new 5x5 list that has M’s in the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells (adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint: short-circuiting may be helpful for avoiding index-out-of-range errors.]
0 M 0 M 0 		1 M 3 M 1
0 0 M 0 0 		1 2 M 2 1
0 0 0 0 0 		2 3 2 1 0
M M 0 0 0 		M M 2 1 1
0 0 0 M 0   	2 2 2 M 1
"""
"""
[i-1][j-1]		[i-1][j]		[j-1][j+1]
[i][j-1]		[i][j]			[i][j+1]
[i+1][j-1]		[i+1][j]		[i+1][j+1]
"""
print('*'*80)

from pprint import pprint
from random import randint

field = [[0 for j in range(5)] for i in range(5)]

print('Field before mine is set:')
for i in range(5):
	for j in range(5):
		print(field[i][j], end=' ')
	print()

temp = 6 #Place the mines at random loations in the field
while temp:
	temp -= 1
	x = randint(0, 4)
	y = randint(0, 4)
	field[x][y] = 'M'
print('Field after mine is set:')
for i in range(5):
	for j in range(5):
		print(field[i][j], end=' ')
	print()

print('Revealed mine field:')

for r in range(5):
	for c in range(5):
		if field[r][c] == 0: #If the cell doesn't contain mine
			for r1 in range(-1, 2):
				if r + r1 in range(5):
					for c1 in range(-1, 2):
						if c + c1 in range(5) and (r1 or c1): #check if neighboring cell exist
							if field[r + r1][c + c1] == 'M':
								field[r][c] += 1

for i in range(5):
	for j in range(5):
		print(field[i][j], end=' ')
	print()

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial2:
********************************************************************************
Field before mine is set:
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
Field after mine is set:
0 0 0 0 0 
0 0 M 0 M 
0 0 0 M 0 
0 M M 0 0 
0 0 M 0 0 
Revealed mine field:
0 1 1 2 1 
0 1 M 3 M 
1 3 4 M 2 
1 M M 3 1 
1 3 M 2 0 
********************************************************************************

@@@@ Trial2:
********************************************************************************
Field before mine is set:
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
Field after mine is set:
0 M M 0 0 
0 0 0 M 0 
0 0 0 0 0 
M 0 0 0 0 
M 0 0 0 0 
Revealed mine field:
1 M M 2 1 
1 2 3 M 1 
1 1 1 1 1 
M 2 0 0 0 
M 2 0 0 0 
********************************************************************************
"""