"""
bhch10exrc05.py: Use the following two lists and the format method to create a list of card names in the format card value of suit name (for example, 'Two of Clubs').

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
"""
print('*'*80)

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

for i in values:
	print('{:5s} of {:6s} | {:5s} of {:8s} | {:5s} of {:5s} | {:5s} of {:6s}'.format(i, suits[0], i, suits[1], i, suits[2], i, suits[3]))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
One   of Hearts | One   of Diamonds | One   of Clubs | One   of Spades
Two   of Hearts | Two   of Diamonds | Two   of Clubs | Two   of Spades
Three of Hearts | Three of Diamonds | Three of Clubs | Three of Spades
Four  of Hearts | Four  of Diamonds | Four  of Clubs | Four  of Spades
Five  of Hearts | Five  of Diamonds | Five  of Clubs | Five  of Spades
Six   of Hearts | Six   of Diamonds | Six   of Clubs | Six   of Spades
Seven of Hearts | Seven of Diamonds | Seven of Clubs | Seven of Spades
Eight of Hearts | Eight of Diamonds | Eight of Clubs | Eight of Spades
Nine  of Hearts | Nine  of Diamonds | Nine  of Clubs | Nine  of Spades
Ten   of Hearts | Ten   of Diamonds | Ten   of Clubs | Ten   of Spades
Jack  of Hearts | Jack  of Diamonds | Jack  of Clubs | Jack  of Spades
Queen of Hearts | Queen of Diamonds | Queen of Clubs | Queen of Spades
King  of Hearts | King  of Diamonds | King  of Clubs | King  of Spades
Ace   of Hearts | Ace   of Diamonds | Ace   of Clubs | Ace   of Spades
********************************************************************************
"""