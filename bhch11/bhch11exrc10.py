"""
bhch11exrc10.py: Using the card dictionary from earlier in the chapter run a Monte Carlo simulation to estimate the probability of being dealt a flush in a five card hand. See Exercise 32 of Chapter 10 (bhch10exrc32.py) for more about Monte Carlo simulations.
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

flush = 0
three_of_a_kind = 0
pair = 0
straight = 0

count = 100
current = 0
while current < count:
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
		flush += 1
		#print('It is a flush!!!')
	if hand_value.count(hand_value[0]) == 3:
		three_of_a_kind += 1
		#print('It is \'three of a kind\'!!')
	else:
		if hand_value.count(hand_value[0]) == 2 or hand_value.count(hand_value[1]) == 2:
			pair += 1
			#print('It is a Pair!!')
	hand_value.sort()
	for i in range(hand_value[0],hand_value[0]+3):#(min(hand_value, max(hand_value)+1))
		if i not in hand_value:
			break
	else:
		straight += 1
		#print('It is a stright!!')
	"""
	print('The hand:')
	for i in range(3):
		print('{:}. {:} of {:}'.format((i+1), hand[i]['value'], hand[i]['suit']))
	"""
	current += 1

print()
print('Flush appeared {:} times out of {:} trials and the probability is {:6.2f}.'.format(flush, count, flush*100/count))
print('three-of-a-kind appeared {:} times out of {:} trials and the probability is {:6.2f}.'.format(three_of_a_kind, count, three_of_a_kind*100/count))
print('Pair appeared {:} times out of {:} trials and the probability is {:6.2f}.'.format(pair, count, pair*100/count))
print('straight appeared {:} times out of {:} trials and the probability is {:6.2f}.'.format(straight, count, straight*100/count))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************

Flush appeared 8 times out of 100 trials and the probability is   8.00.
three-of-a-kind appeared 0 times out of 100 trials and the probability is   0.00.
Pair appeared 16 times out of 100 trials and the probability is  16.00.
straight appeared 3 times out of 100 trials and the probability is   3.00.
********************************************************************************

@@@@ Trial2:
********************************************************************************

Flush appeared 2 times out of 100 trials and the probability is   2.00.
three-of-a-kind appeared 0 times out of 100 trials and the probability is   0.00.
Pair appeared 20 times out of 100 trials and the probability is  20.00.
straight appeared 2 times out of 100 trials and the probability is   2.00.
********************************************************************************

@@@@ Trial3:
********************************************************************************

Flush appeared 3 times out of 100 trials and the probability is   3.00.
three-of-a-kind appeared 0 times out of 100 trials and the probability is   0.00.
Pair appeared 22 times out of 100 trials and the probability is  22.00.
straight appeared 1 times out of 100 trials and the probability is   1.00.
********************************************************************************
"""