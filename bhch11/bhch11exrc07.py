"""
bhch11exrc07.py: Create a 5x5 list of numbers. Then write a program that creates a dictionary whose keys are the numbers and whose values are the how many times the number occurs. Then print the three most common numbers.
"""
print('*'*80)

from random import randint
from pprint import pprint

mat = [[randint(1, 9) for j in range(5)] for i in range(5)]
pprint(mat)

mat2 = [j for i in mat for j in i]

dict = {}
for i in range(1, 10):
	dict[i] = mat2.count(i)

print('Dictionary dict:', dict)
l = [(dict[i], i) for i in dict]
l.sort(reverse = True)

print('The 3 numbers that appeared most.')
for i in range(3):
	print('Key: {:}, Value: {:}'.format(l[i][1], l[i][0]))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
[[4, 4, 4, 9, 2],
 [4, 6, 8, 7, 6],
 [5, 9, 4, 4, 1],
 [8, 5, 4, 3, 4],
 [6, 9, 9, 1, 9]]
Dictionary dict: {1: 2, 2: 1, 3: 1, 4: 8, 5: 2, 6: 3, 7: 1, 8: 2, 9: 5}
The 3 numbers that appeared most.
Key: 4, Value: 8
Key: 9, Value: 5
Key: 6, Value: 3
********************************************************************************
"""