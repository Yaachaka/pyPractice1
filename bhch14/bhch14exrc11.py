"""
bhch14exrc11.py: Write a class called Poker_hand that has a field that is a list of Card objects. There should be the following self-explanatory methods:

	has_royal_flush, has_straight_flush, has_four_of_a_kind,
	has_full_house, has_flush, has_straight,
	has_three_of_a_kind, has_two_pair, has_pair

There should also be a method called best that returns a string indicating what the best hand is that can be made from those cards.
"""
print('*'*80)

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
from random import random, randint, shuffle, sample
#------------------------------------------------------------------------------------
class Card:#Each card's specification
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	
	def __str__(self):#To print card
		names = ['Jack', 'Queen', 'King', 'Ace']
		if self.value <= 10:
			return '{} of {}'.format(self.value, self.suit)
		else:
			return '{} of {}'.format(names[self.value-11], self.suit)
#------------------------------------------------------------------------------------
class Card_group:
	def __init__(self, cards=[]):
		self.cards = cards
	
	def nextCard(self):
		return self.cards.pop(0)
	
	def hasCard(self):
		return len(self.cards)>0
	
	def size(self):
		return len(self.cards)
	
	def shuffle(self):
		shuffle(self.cards)
#------------------------------------------------------------------------------------
class Standard_deck(Card_group):#Inherited from Card_group class
	def __init__(self):
		self.cards = []
		for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
			for v in range(2,15):
				self.cards.append(Card(v, s))
#------------------------------------------------------------------------------------
class Poker_hand(Card_group):
	def __init__(self, hand):
		self.hand = hand[:]
		self.has_royal_flush = 0
		self.has_straight_flush = 0
		self.has_four_of_a_kind = 0
		self.has_full_house = 0
		self.has_flush = 0
		self.has_straight = 1
		self.has_three_of_a_kind = 0
		self.has_two_pair = 0
		self.has_pair = 0
		self.high = 0
		self.type = 'Stright'

	def __str__(self):
		self.spec()
		for i in self.hand:
			print(i)
		print(self.type)
		return ''
	
	def spec(self):
		#self.hand.sort()
		r_hand = [i.value for i in self.hand]
		r_hand.sort()
		s_hand = [i.suit for i in self.hand]

		for i in range(1, 5):
			if r_hand[i] != r_hand[i-1] + 1:
				self.has_straight = 0
				break
		if s_hand.count(s_hand[0]) == 5:
			self.has_flush = 1
			self.type = 'Flush'
		
		if self.has_flush and self.has_straight:
			if r_hand[0] == 10:
				self.has_royal_flush = 1
				self.type = 'Royal Flush'
			else:
				self.has_straight_flush = 1
				self.type = 'Straight Flush'
			self.has_flush = self.has_straight = 0
		
		temp = self.has_flush + self.has_straight + self.has_royal_flush + self.has_straight_flush

		if not temp:
			if r_hand.count(r_hand[0]) == 4 or r_hand.count(r_hand[1]) == 4:
				self.has_four_of_a_kind = 1
				self.type = 'Four of a kind'
			else:
				temp2 = {}
				for i in r_hand:
					if i not in temp2:
						temp2[i] = r_hand.count(i)
				l = len(temp2)
				if l == 5:
					self.high = 1
					self.type = 'High card'
				elif l == 2:
					self.has_full_house = 1
					self.type = 'Full house'
				elif l == 3:
					for i in temp2:
						if temp2[i] == 3:
							self.has_three_of_a_kind = 1
							self.type = 'Three of a kind'
							break
					if not self.has_three_of_a_kind:
						self.has_two_pair = 1
						self.type = 'Two pairs'
				elif l == 4:
					self.has_pair = 1
					self.type = 'Pair'


#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
deck = Standard_deck()
deck.shuffle()

hand1 = Poker_hand(sample(deck.cards, 5))
print(hand1)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
7 of Clubs
Jack of Spades
5 of Clubs
8 of Spades
5 of Hearts
Pair

********************************************************************************

Hanumantha@Hanu /cygdrive/f/try/gitpracts2/pyPractice1
$ make
@@@@ Trial1:
********************************************************************************
Ace of Hearts
Queen of Diamonds
3 of Diamonds
2 of Diamonds
King of Hearts
High card

********************************************************************************

@@@@ Trial2:
********************************************************************************
Ace of Diamonds
King of Diamonds
4 of Diamonds
10 of Hearts
6 of Diamonds
High card

********************************************************************************

@@@@ Trial3:
********************************************************************************
7 of Hearts
Jack of Spades
7 of Spades
9 of Diamonds
9 of Spades
Two pairs

********************************************************************************

@@@@ Trial4:
********************************************************************************
3 of Spades
8 of Clubs
King of Diamonds
5 of Hearts
3 of Clubs
Pair

********************************************************************************

@@@@ Trial5:
********************************************************************************
King of Hearts
10 of Spades
Jack of Spades
9 of Clubs
Queen of Clubs
Stright

********************************************************************************

@@@@ Trial6:
********************************************************************************
Queen of Hearts
Queen of Spades
Jack of Diamonds
Queen of Diamonds
6 of Hearts
Three of a kind

********************************************************************************

@@@@ Trial7:
********************************************************************************
Ace of Diamonds
9 of Hearts
Ace of Spades
Ace of Hearts
9 of Clubs
Full house

********************************************************************************

@@@@ Trial8:

"""