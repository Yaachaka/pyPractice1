"""
bhch08exrc18.py: Write a program that creates a 10x10 list of random integers between 1 and 100. Then do the following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column.
"""
print('*'*80)

from random import randint

l1 = [[randint(1, 100) for j in range(10)] for i in range(10)]

print('(a) Print the list:')
print(l1)

print('(b) Find the largest value in the third row:', max(l1[2]))

print('(c) Find the smallest value in the sixth column:', min([l1[i][5] for i in range(10)]))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial 1:
********************************************************************************
(a) Print the list:
[[51, 30, 44, 8, 7, 66, 66, 4, 12, 10], [45, 32, 77, 55, 47, 42, 95, 24, 14, 85], [85, 7, 90, 10, 39, 44, 57, 50, 50, 37], [63, 1, 48, 25, 6, 86, 32, 29, 18, 50], [13, 57, 1, 9, 44, 25, 24, 8, 37, 26], [47, 60, 99,
39, 35, 51, 53, 20, 52, 25], [27, 24, 91, 6, 78, 1, 48, 49, 14, 93], [70, 2, 78, 28, 24, 62, 52, 54, 87, 74], [100, 10, 37, 62, 88, 62, 94, 78, 77, 25], [95, 84, 50, 89, 19, 99, 82, 74, 68, 70]]
(b) Find the largest value in the third row: 90
(c) Find the smallest value in the sixth column: 1
********************************************************************************

@@@@ Trial 2:
********************************************************************************
(a) Print the list:
[[71, 71, 78, 99, 4, 44, 100, 56, 73, 48], [84, 33, 88, 31, 96, 25, 31, 76, 100, 24], [45, 5, 9, 54, 2, 84, 11, 65, 77, 49], [53, 67, 21, 9, 7, 99, 88, 75, 44, 65], [64, 1, 43, 10, 68, 4, 7, 45, 83, 87], [41, 67, 93, 29, 90, 14, 5, 75, 75, 96], [34, 77, 82, 83, 51, 92, 64, 77, 58, 55], [6, 84, 85, 45, 50, 63, 22, 53, 14, 55], [20, 51, 75, 47, 61, 70, 28, 53, 16, 91], [21, 96, 26, 83, 46, 78, 5, 46, 32, 26]]
(b) Find the largest value in the third row: 84
(c) Find the smallest value in the sixth column: 4
********************************************************************************
"""