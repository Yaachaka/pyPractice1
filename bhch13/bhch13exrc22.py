"""
bhch13exrc22.py: A Tic-tac-toe board can be represented be a 3x3 two-dimensional list, where zeroes stand for empty cells, ones stand for X’s and twos stand for O’s.
(a) Write a function that is given such a list and randomly chooses a spot in which to place a 2. The spot chosen must currently be a 0 and a spot must be chosen.
(b) Write a function that is given such a list and checks to see if someone has won. Return True if there is a winner and False otherwise.
"""
print('*'*80)

from random import randint

board = [str(j) for j in range(9)]
possibs = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 4, 6], [0, 4, 8]]

def print_board():
	print('Current game state: ')
	for i in range(0, 9, 3):
		print('-'*13)
		print('|{:^3}|{:^3}|{:^3}|'.format(board[i], board[i+1], board[i+2]))
	print('-'*13)

def u_choice():
	while True:
		slot = eval(input('Select from available slot: '))%9
		if board[slot] in 'XO':
			print('That slot is already taken')
		else:
			board[slot] = u_symbol
			user.append(slot)
			user.sort()
			break

def s_choice():
	while True:
		slot = randint(0, 8)
		if board[slot] not in 'XO':
			board[slot] = s_symbol
			system.append(slot)
			system.sort()
			break

print('Welcome to Tic-Tac-Toe game:')
print('(a) Part a:')
u_symbol = 'X'
s_symbol = 'O'
if input('Choose your symbol: default-X, type O to choose O: ').upper() == 'O':
	u_symbol = 'O'
	s_symbol = 'X'
print_board()

user = []
system = []


#User first choice
u_choice()

#System first choice
s_choice()
print_board()

#User second choice
u_choice()

#System second choice
s_choice()
print_board()

#User third choice
u_choice()

if user in possibs:
	print('You win')
else:
	#System third choice
	s_choice()
print_board()
if system in possibs:
	print('Computer wins')


print('\n(b) To see if someone won (True if won else False): {:}.'.format(user in possibs or system in possibs))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Welcome to Tic-Tac-Toe game:
(a) Part a:
Choose your symbol: default-X, type O to choose O: x
Current game state:
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Select from available slot: 2
Current game state:
-------------
| O | 1 | X |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Select from available slot: 6
Current game state:
-------------
| O | 1 | X |
-------------
| O | 4 | 5 |
-------------
| X | 7 | 8 |
-------------
Select from available slot: 4
You win
Current game state:
-------------
| O | 1 | X |
-------------
| O | X | 5 |
-------------
| X | 7 | 8 |
-------------

(b) To see if someone won (True if won else False): True.
********************************************************************************
"""