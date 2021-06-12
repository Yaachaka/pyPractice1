"""
bhch09exrc12.py: Write a program in which you have a list that contains seven integers that can be 0 or 1. Find the first nonzero entry in the list and change it to a 1. If there are no nonzero entries, print a message saying so.
"""
print('*'*80)

from random import randint

list1 = [randint(0,1) for i in range(7)]
print('Before: list1:', list1)

count = list1.count(1)
while count != 7:
	ind = randint(0, len(list1)-1)
	list1[ind] = 1
	count = list1.count(1)

print('After: list1:', list1)

print('*'*80)
"""PROGRAM OUTPUT

@@@@ Trial1:
********************************************************************************
Before: list1: [0, 0, 0, 0, 0, 1, 0]
After: list1: [1, 1, 1, 1, 1, 1, 1]
********************************************************************************

@@@@ Trial2:
********************************************************************************
Before: list1: [0, 0, 1, 0, 0, 0, 1]
After: list1: [1, 1, 1, 1, 1, 1, 1]
********************************************************************************
"""