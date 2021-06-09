"""
bhch08exrc22.py: The following is useful as part of a program to play Battleship. Suppose you have a 5 x 5 list that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the list at that row and column is a one, the program should print Hit and otherwise it should print Miss.
"""
print('*'*80)

from random import randint

field = [[randint(0,1) for i in range(5)] for i in range(5)]
row = eval(input('Enter integer X co-ordinate(0 to 4): '))%5
column = eval(input('Enter integer Y co-ordinate(0 to 4): '))%5

if field[row][column]:
	print('That\'s a Hit!!!')
else:
	print('That\'s a miss!!!')

print('Battleships\' locations:', field)


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter integer X co-ordinate(0 to 4): 3
Enter integer Y co-ordinate(0 to 4): 2
That's a Hit!!!
Battleships' locations: [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [1, 0, 0, 0, 1]]
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter integer X co-ordinate(0 to 4): 1
Enter integer Y co-ordinate(0 to 4): 4
That's a miss!!!
Battleships' locations: [[1, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1]]
********************************************************************************
"""