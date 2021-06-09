"""
bhch08exrc17.py: Write a program that finds the average of all of the entries in a 4 x 4 list of integers.
"""
print('*'*80)

from random import randint

l = [[randint(1, 10) for j in range(4)] for i in range(4)]
print('l =', l)

l2 = [j for i in l for j in i]

print('Sum =', sum(l2))
print('len =', len(l2))
print('average = ', sum(l2)/len(l2))


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial 1:
********************************************************************************
l = [[9, 10, 7, 9], [6, 8, 2, 3], [8, 9, 1, 10], [4, 6, 2, 9]]
Sum = 103
len = 16
average =  6.4375
********************************************************************************

@@@@ Trial 2:
********************************************************************************
l = [[1, 9, 5, 8], [7, 4, 9, 7], [2, 2, 9, 9], [6, 9, 10, 3]]
Sum = 100
len = 16
average =  6.25
********************************************************************************"""