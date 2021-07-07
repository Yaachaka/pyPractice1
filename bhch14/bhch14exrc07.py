"""
bhch14exrc07.py: Use the Standard_deck class of this section to create a simplified version of the game War. In this game, there are two players. Each starts with half of a deck. The players each deal the top card from their decks and whoever has the higher card wins the other player’s cards and adds them to the bottom of his deck. If there is a tie, the two cards are eliminated from play (this differs from the actual game, but is simpler to program). The game ends when one player runs out of cards.
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
deck = Standard_deck()
deck.shuffle()

l = len(deck.cards)
#Each start with half of  deck
player1 = Card_group(deck.cards[:l//2])
player2 = Card_group(deck.cards[l//2:])
l1 = len(player1.cards)
l2 = len(player2.cards)
eliminated_cards = []

while (l1 and l2):
	#Get card from top from each player
	p1_card = player1.nextCard()
	p2_card = player2.nextCard()

	#Compare the cards
	if p1_card.value == p2_card.value:
		eliminated_cards.append(p1_card)
		eliminated_cards.append(p2_card)
	elif p1_card.value > p2_card.value:
		player1.cards.insert(0, p1_card)
		player1.cards.append(p2_card)
	else:
		player2.cards.insert(0, p2_card)
		player2.cards.append(p1_card)
	l1 = len(player1.cards)
	l2 = len(player2.cards)

if l1:
	print('Player1 wins with {} cards in hand.'.format(l1))
else:
	print('Player2 wins with {} cards in hand.'.format(l2))
#------------------------------------------------------------------------------------
print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Player2 wins with 48 cards in hand.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Player1 wins with 42 cards in hand.
********************************************************************************
"""