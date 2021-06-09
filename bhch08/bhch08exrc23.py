"""
bhch08exrc23.py: This exercise is useful in creating a Memory game. Randomly generate a 6 x 6 list of assorted characters such that there are exactly two of each character. An example is shown below.

@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x
"""
print('*'*80)

from random import shuffle, sample

chars = 'ABCDEFGHIJKLMNOPQRSTUVXYZ!@#$%^&*()'
few1 = sample(list(chars), 18)
few2 = few1 * 2
shuffle(few2)

mat = [few2[i:i+6] for i in range(0,36,6)]

print(mat)

for i in range(6):
	print('\n')
	for j in range(6):
		print(mat[i][j], end=' ')

print()

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
[['&', 'H', 'U', 'H', 'T', '!'], ['^', 'D', '%', '$', 'K', 'B'], [')', 'Y', '^', 'V', '$', '*'], ['Y', 'K', '(', '%', 'S', 'A'], ['&', 'T', 'B', 'S', '*', 'D'], ['(', 'A', ')', 'V', 'U', '!']]


& H U H T !

^ D % $ K B

) Y ^ V $ *

Y K ( % S A

& T B S * D

( A ) V U !
********************************************************************************
"""