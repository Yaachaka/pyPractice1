"""
bhch11exrc08.py: Using the card dictionary from earlier in this chapter, create a simple card game that deals two players three cards each. The player with the highest card wins. If there is a tie, then compare the second highest card and, if necessary, the third highest. If all three cards have the same value, then the game is a draw.
"""
print('*'*80)

from pprint import pprint
from random import shuffle, randint

deck = [{'value':i, 'suit':c} for c in ['spades', 'clubs', 'hearts', 'diamonds'] for i in range(2,15)]
print('Before shuffle:')
pprint(deck)
shuffle(deck)
print('-'*60)
print('After shuffle:')
pprint(deck)
print('-'*60)

for i in range(3):
	player1 = randint(0, 51)
	player2 = randint(0, 51)
	while player1 == player2:
		player2 = randint(0, 51)
	player1 = deck[player1]
	player2 = deck[player2]
	print('Player1\'s hand', player1)
	print('Player2\'s hand', player2)
	v = 'value'
	if player1[v] != player2[v]:
		if player1[v] > player2[v]:
			print('Player1 wins.')
		else:
			print('Player2 wins.')
		break
else:
	print('The game is draw.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Before shuffle:
[{'suit': 'spades', 'value': 2},
 {'suit': 'spades', 'value': 3},
 {'suit': 'spades', 'value': 4},
 {'suit': 'spades', 'value': 5},
 {'suit': 'spades', 'value': 6},
 {'suit': 'spades', 'value': 7},
 {'suit': 'spades', 'value': 8},
 {'suit': 'spades', 'value': 9},
 {'suit': 'spades', 'value': 10},
 {'suit': 'spades', 'value': 11},
 {'suit': 'spades', 'value': 12},
 {'suit': 'spades', 'value': 13},
 {'suit': 'spades', 'value': 14},
 {'suit': 'clubs', 'value': 2},
 {'suit': 'clubs', 'value': 3},
 {'suit': 'clubs', 'value': 4},
 {'suit': 'clubs', 'value': 5},
 {'suit': 'clubs', 'value': 6},
 {'suit': 'clubs', 'value': 7},
 {'suit': 'clubs', 'value': 8},
 {'suit': 'clubs', 'value': 9},
 {'suit': 'clubs', 'value': 10},
 {'suit': 'clubs', 'value': 11},
 {'suit': 'clubs', 'value': 12},
 {'suit': 'clubs', 'value': 13},
 {'suit': 'clubs', 'value': 14},
 {'suit': 'hearts', 'value': 2},
 {'suit': 'hearts', 'value': 3},
 {'suit': 'hearts', 'value': 4},
 {'suit': 'hearts', 'value': 5},
 {'suit': 'hearts', 'value': 6},
 {'suit': 'hearts', 'value': 7},
 {'suit': 'hearts', 'value': 8},
 {'suit': 'hearts', 'value': 9},
 {'suit': 'hearts', 'value': 10},
 {'suit': 'hearts', 'value': 11},
 {'suit': 'hearts', 'value': 12},
 {'suit': 'hearts', 'value': 13},
 {'suit': 'hearts', 'value': 14},
 {'suit': 'diamonds', 'value': 2},
 {'suit': 'diamonds', 'value': 3},
 {'suit': 'diamonds', 'value': 4},
 {'suit': 'diamonds', 'value': 5},
 {'suit': 'diamonds', 'value': 6},
 {'suit': 'diamonds', 'value': 7},
 {'suit': 'diamonds', 'value': 8},
 {'suit': 'diamonds', 'value': 9},
 {'suit': 'diamonds', 'value': 10},
 {'suit': 'diamonds', 'value': 11},
 {'suit': 'diamonds', 'value': 12},
 {'suit': 'diamonds', 'value': 13},
 {'suit': 'diamonds', 'value': 14}]
------------------------------------------------------------
After shuffle:
[{'suit': 'spades', 'value': 8},
 {'suit': 'clubs', 'value': 5},
 {'suit': 'spades', 'value': 5},
 {'suit': 'clubs', 'value': 2},
 {'suit': 'spades', 'value': 9},
 {'suit': 'spades', 'value': 14},
 {'suit': 'diamonds', 'value': 11},
 {'suit': 'diamonds', 'value': 8},
 {'suit': 'clubs', 'value': 13},
 {'suit': 'diamonds', 'value': 10},
 {'suit': 'clubs', 'value': 10},
 {'suit': 'spades', 'value': 7},
 {'suit': 'hearts', 'value': 9},
 {'suit': 'spades', 'value': 12},
 {'suit': 'diamonds', 'value': 5},
 {'suit': 'hearts', 'value': 10},
 {'suit': 'clubs', 'value': 4},
 {'suit': 'spades', 'value': 11},
 {'suit': 'spades', 'value': 13},
 {'suit': 'hearts', 'value': 12},
 {'suit': 'spades', 'value': 4},
 {'suit': 'spades', 'value': 2},
 {'suit': 'diamonds', 'value': 7},
 {'suit': 'clubs', 'value': 6},
 {'suit': 'hearts', 'value': 3},
 {'suit': 'diamonds', 'value': 4},
 {'suit': 'diamonds', 'value': 13},
 {'suit': 'clubs', 'value': 9},
 {'suit': 'diamonds', 'value': 2},
 {'suit': 'spades', 'value': 3},
 {'suit': 'diamonds', 'value': 9},
 {'suit': 'hearts', 'value': 5},
 {'suit': 'hearts', 'value': 4},
 {'suit': 'clubs', 'value': 8},
 {'suit': 'diamonds', 'value': 6},
 {'suit': 'hearts', 'value': 2},
 {'suit': 'clubs', 'value': 3},
 {'suit': 'hearts', 'value': 11},
 {'suit': 'hearts', 'value': 14},
 {'suit': 'clubs', 'value': 14},
 {'suit': 'hearts', 'value': 8},
 {'suit': 'spades', 'value': 10},
 {'suit': 'clubs', 'value': 12},
 {'suit': 'diamonds', 'value': 3},
 {'suit': 'clubs', 'value': 11},
 {'suit': 'hearts', 'value': 7},
 {'suit': 'spades', 'value': 6},
 {'suit': 'diamonds', 'value': 14},
 {'suit': 'hearts', 'value': 13},
 {'suit': 'hearts', 'value': 6},
 {'suit': 'clubs', 'value': 7},
 {'suit': 'diamonds', 'value': 12}]
------------------------------------------------------------
Player1's hand {'value': 7, 'suit': 'hearts'}
Player2's hand {'value': 11, 'suit': 'clubs'}
Player2 wins.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Before shuffle:
[{'suit': 'spades', 'value': 2},
 {'suit': 'spades', 'value': 3},
 {'suit': 'spades', 'value': 4},
 {'suit': 'spades', 'value': 5},
 {'suit': 'spades', 'value': 6},
 {'suit': 'spades', 'value': 7},
 {'suit': 'spades', 'value': 8},
 {'suit': 'spades', 'value': 9},
 {'suit': 'spades', 'value': 10},
 {'suit': 'spades', 'value': 11},
 {'suit': 'spades', 'value': 12},
 {'suit': 'spades', 'value': 13},
 {'suit': 'spades', 'value': 14},
 {'suit': 'clubs', 'value': 2},
 {'suit': 'clubs', 'value': 3},
 {'suit': 'clubs', 'value': 4},
 {'suit': 'clubs', 'value': 5},
 {'suit': 'clubs', 'value': 6},
 {'suit': 'clubs', 'value': 7},
 {'suit': 'clubs', 'value': 8},
 {'suit': 'clubs', 'value': 9},
 {'suit': 'clubs', 'value': 10},
 {'suit': 'clubs', 'value': 11},
 {'suit': 'clubs', 'value': 12},
 {'suit': 'clubs', 'value': 13},
 {'suit': 'clubs', 'value': 14},
 {'suit': 'hearts', 'value': 2},
 {'suit': 'hearts', 'value': 3},
 {'suit': 'hearts', 'value': 4},
 {'suit': 'hearts', 'value': 5},
 {'suit': 'hearts', 'value': 6},
 {'suit': 'hearts', 'value': 7},
 {'suit': 'hearts', 'value': 8},
 {'suit': 'hearts', 'value': 9},
 {'suit': 'hearts', 'value': 10},
 {'suit': 'hearts', 'value': 11},
 {'suit': 'hearts', 'value': 12},
 {'suit': 'hearts', 'value': 13},
 {'suit': 'hearts', 'value': 14},
 {'suit': 'diamonds', 'value': 2},
 {'suit': 'diamonds', 'value': 3},
 {'suit': 'diamonds', 'value': 4},
 {'suit': 'diamonds', 'value': 5},
 {'suit': 'diamonds', 'value': 6},
 {'suit': 'diamonds', 'value': 7},
 {'suit': 'diamonds', 'value': 8},
 {'suit': 'diamonds', 'value': 9},
 {'suit': 'diamonds', 'value': 10},
 {'suit': 'diamonds', 'value': 11},
 {'suit': 'diamonds', 'value': 12},
 {'suit': 'diamonds', 'value': 13},
 {'suit': 'diamonds', 'value': 14}]
------------------------------------------------------------
After shuffle:
[{'suit': 'spades', 'value': 3},
 {'suit': 'spades', 'value': 12},
 {'suit': 'spades', 'value': 8},
 {'suit': 'hearts', 'value': 6},
 {'suit': 'clubs', 'value': 14},
 {'suit': 'diamonds', 'value': 2},
 {'suit': 'hearts', 'value': 3},
 {'suit': 'diamonds', 'value': 13},
 {'suit': 'hearts', 'value': 8},
 {'suit': 'hearts', 'value': 4},
 {'suit': 'hearts', 'value': 5},
 {'suit': 'diamonds', 'value': 6},
 {'suit': 'spades', 'value': 13},
 {'suit': 'clubs', 'value': 7},
 {'suit': 'hearts', 'value': 9},
 {'suit': 'spades', 'value': 10},
 {'suit': 'diamonds', 'value': 7},
 {'suit': 'spades', 'value': 6},
 {'suit': 'hearts', 'value': 13},
 {'suit': 'spades', 'value': 2},
 {'suit': 'diamonds', 'value': 9},
 {'suit': 'diamonds', 'value': 5},
 {'suit': 'hearts', 'value': 10},
 {'suit': 'spades', 'value': 5},
 {'suit': 'clubs', 'value': 10},
 {'suit': 'clubs', 'value': 9},
 {'suit': 'hearts', 'value': 2},
 {'suit': 'clubs', 'value': 12},
 {'suit': 'spades', 'value': 14},
 {'suit': 'clubs', 'value': 8},
 {'suit': 'diamonds', 'value': 3},
 {'suit': 'clubs', 'value': 5},
 {'suit': 'clubs', 'value': 11},
 {'suit': 'spades', 'value': 4},
 {'suit': 'spades', 'value': 9},
 {'suit': 'clubs', 'value': 3},
 {'suit': 'diamonds', 'value': 12},
 {'suit': 'hearts', 'value': 7},
 {'suit': 'diamonds', 'value': 14},
 {'suit': 'spades', 'value': 7},
 {'suit': 'diamonds', 'value': 10},
 {'suit': 'clubs', 'value': 4},
 {'suit': 'spades', 'value': 11},
 {'suit': 'clubs', 'value': 2},
 {'suit': 'hearts', 'value': 12},
 {'suit': 'clubs', 'value': 13},
 {'suit': 'diamonds', 'value': 11},
 {'suit': 'diamonds', 'value': 8},
 {'suit': 'hearts', 'value': 14},
 {'suit': 'hearts', 'value': 11},
 {'suit': 'diamonds', 'value': 4},
 {'suit': 'clubs', 'value': 6}]
------------------------------------------------------------
Player1's hand {'value': 14, 'suit': 'clubs'}
Player2's hand {'value': 13, 'suit': 'spades'}
Player1 wins.
********************************************************************************
"""