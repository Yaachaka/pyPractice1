"""
bhch11exrc09.py: Using the card dictionary from earlier in the chapter, deal out three cards. Determine the following:
(a) If the three cards form a flush (all of the same suit)
(b) If there is a three-of-a-kind (all of the same value)
(c) If there is a pair, but not three-of-a-kind
(d) If the three cards form a straight (all in a row, like (2, 3, 4) or (10, Jack, Queen))
"""
print('*'*80)

from pprint import pprint
from random import shuffle, randint

deck = [{'value':i, 'suit':c} for c in ['spades', 'clubs', 'hearts', 'diamonds'] for i in range(2,15)]
#print('Before shuffle:')
#pprint(deck)
shuffle(deck)
#print('-'*60)
#print('After shuffle:')
#pprint(deck)
#print('-'*60)

hand = [randint(0, 51)]
for i in range(1, 3):
	ind = randint(0, 51)
	hand.append(ind)
	while ind in hand[:i]: #Just to avoid repition of same card
		ind = randint(0, 51)
		hand[i] = ind
	
hand_value = []
hand_suit = []
for i in range(3):
	hand[i] = deck[hand[i]]
	hand_value.append(hand[i]['value'])
	hand_suit.append(hand[i]['suit'])

if hand_suit.count(hand_suit[0]) == 3:
	print('It is a flush!!!')
if hand_value.count(hand_value[0]) == 3:
	print('It is \'three of a kind\'!!')
else:
	if hand_value.count(hand_value[0]) == 2 or hand_value.count(hand_value[1]) == 2:
		print('It is a Pair!!')
hand_value.sort()
for i in range(hand_value[0],hand_value[0]+3):#(min(hand_value, max(hand_value)+1))
	if i not in hand_value:
		break
else:
	print('It is a stright!!')

print('The hand:')
for i in range(3):
	print('{:}. {:} of {:}'.format((i+1), hand[i]['value'], hand[i]['suit']))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
The hand:
1. 2 of spades
2. 5 of hearts
3. 8 of clubs
********************************************************************************

@@@@ Trial2:
********************************************************************************
The hand:
1. 10 of hearts
2. 7 of clubs
3. 12 of diamonds
********************************************************************************

@@@@ Trial3:
********************************************************************************
It is a Pair!!
The hand:
1. 9 of spades
2. 2 of hearts
3. 2 of spades
********************************************************************************

@@@@ Trial4:
********************************************************************************
The hand:
1. 2 of diamonds
2. 4 of spades
3. 11 of diamonds
********************************************************************************
"""