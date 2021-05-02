"""
bhch07exrc12.py: Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros, the largest number of zeros in a row. For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
"""
print('*'*80)

from random import randint

l = []
length = 10
longestz = 0
for i in range(length):
	l.append(randint(0,1))

count = 0
for i in range(length):
	if l[i]:
		count = 0
	else:
		count = count + 1
		if count > longestz:
			longestz = count
	
print('List:', l)
print('Longest run of zeroes:', longestz)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
List: [1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
Longest run of zeroes: 2
********************************************************************************

@@@@ Trial2:
********************************************************************************
List: [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
Longest run of zeroes: 4
********************************************************************************

@@@@ Trial3:
********************************************************************************
List: [1, 1, 0, 1, 0, 1, 0, 1, 0, 0]
Longest run of zeroes: 2
********************************************************************************
"""