"""
bhch09exrc18.py: Randomly generate a 6 x 6 list that has exactly 12 ones placed in random locations in the list. The rest of the entries should be zeroes.
"""
print('*'*80)

from random import randint

l1 = [[0]*6]*6
print('l1(Before):')
l2 = [j for i in l1 for j in i]
for i in range(6):
	print('0 '*6)

print('\nl1(After):')
count1 = l2.count(1)

while True:
	ind = randint(0, 35)
	if not l2[ind]:
		l2[ind] = 1
		count1 = l2.count(1)
		if count1 == 12:
			break

l1 = [l1[i:i+6] for i in range(6)]
for i in range(36):
	if not i%6:
		print()
	print(l2[i], end=' ')

print()

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
l1(Before):
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

l1(After):

0 0 0 0 1 0
0 0 1 1 0 0
0 1 1 0 0 0
0 0 1 0 0 1
1 0 1 1 0 1
0 0 0 1 0 0
********************************************************************************
"""