"""
bhch14exrc08.py: Write a class that inherits from the Card_group class of this chapter. The class should represent a deck of cards that contains only hearts and spaces, with only the cards 2 through 10 in each suit. Add a method to the class called next2 that returns the top two cards from the deck.
"""
print('*'*80)

#------------------------------------------------------------------------------------
from random import random, randint, shuffle
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
class Pinochle_deck(Card_group):#Inherited from Card_group class
	def __init__(self):
		self.cards = []
		for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']*2:
			for v in range(9,15):
				self.cards.append(Card(v, s))
#------------------------------------------------------------------------------------
class type2_deck(Card_group):#Inherited from Card_group class
	def __init__(self):
		self.cards = []
		for s in ['Hearts', 'Spades']:
			for v in range(2,11):
				self.cards.append(Card(v, s))
		
	def next2(self):
		return self.cards[:2]
#---------------------------------------------------------------------------
deck = type2_deck()
deck.shuffle()

print('Whole deck:')
for i in deck.cards:
	print(i)

print('Two cards from the top of the deck:')
for i in deck.next2():
	print(i)
#------------------------------------------------------------------------------------


print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Whole deck:
9 of Spades
3 of Hearts
4 of Hearts
7 of Spades
8 of Hearts
2 of Hearts
5 of Spades
6 of Hearts
6 of Spades
8 of Spades
9 of Hearts
2 of Spades
7 of Hearts
5 of Hearts
4 of Spades
10 of Spades
10 of Hearts
3 of Spades
Two cards from the top of the deck:
9 of Spades
3 of Hearts
********************************************************************************
"""