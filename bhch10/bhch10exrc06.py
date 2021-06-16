"""
bhch10exrc06.py: Write a program that uses a boolean flag variable in determining whether two lists have any items in common.
"""
print('*'*80)

from random import sample

chars = 'abcdefghijklmnopqrstuvwxyz'
l1 = sample(list(chars), 5)
l2 = sample(list(chars), 5)
print(l1)
print(l2)

flag = False
for i in l1:
	if l2.count(i):
		flag = True
		break

print('Atleast one item from each list is common:', flag)

print('*'*80)
"""PROGRAM OUTPUT

@@@@ Trial1:
********************************************************************************
['y', 'd', 'g', 'm', 'v']
['q', 'n', 'j', 'g', 'i']
Atleast one item from each list is common: True
********************************************************************************

@@@@ Trial2:
********************************************************************************
['k', 't', 'e', 'l', 'r']
['y', 's', 'q', 'w', 'i']
Atleast one item from each list is common: False
********************************************************************************
"""