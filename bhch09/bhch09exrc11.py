"""
bhch09exrc11.py: Write a program that starts with an 5 x 5 list of zeroes and randomly changes exactly ten of those zeroes to ones.
"""
print('*'*80)

from random import randint

mat = [[0]*5 for i in range(5)]
print('mat:', mat)

mat2 = [j for i in mat for j in i] #convertting to 1 dimension
print('1-D equivalent to mat:', mat2)
count = mat2.count(1)

while count != 10:
	ind = randint(0, len(mat2)-1)
	mat2[ind] = 1
	count = mat2.count(1)

print('mat2:', mat2)

mat = [mat2[i:i+5] for i in range(0,25,5)]
print('mat:', mat)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
mat: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
1-D equivalent to mat: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mat2: [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]
mat: [[0, 1, 0, 1, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 1, 0]]
********************************************************************************

@@@@ Trial2:
********************************************************************************
mat: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
1-D equivalent to mat: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mat2: [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
mat: [[0, 1, 0, 1, 1], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 0]]
********************************************************************************
"""