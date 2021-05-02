"""
bhch07exrc10.py: 
Write a program that rotates the elements of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.
"""
print('*'*80)

L = eval(input('Enter a list: '))
L2 = []

for i in range(len(L)):
	L2.append(L[-1 + i])

print('Rotated list:', L2)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter a list: 1,2,3,4,5,6
Rotated list: [6, 1, 2, 3, 4, 5]
********************************************************************************
"""