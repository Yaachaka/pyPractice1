"""
bhch08exrc19.py: Write a program that creates and prints an 8 x 8 list whose entries alternate between 1 and 2 in a checkerboard pattern, starting with 1 in the upper left corner.
"""
print('*'*80)

l1 = [[2**(j%2) for j in range(8)] for i in range(8)]
print(l1)


print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
[[1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2]]
********************************************************************************
"""