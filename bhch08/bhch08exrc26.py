"""
bhch08exrc26.py: We usually refer to the entries of a two-dimensional list by their row and column, like below on the left. Another way is shown below on the right.

(0,0) (0,1) (0,2)            0 1 2
(1,0) (1,1) (1,2)            3 4 5
(2,0) (2,1) (2,2)            6 7 8

(a) Write some code that translates from the left representation to the right one. The // and % operators will be useful. Be sure your code works for arrays of any size.
(b) Write some code that translates from the right representation to the left one.
"""
print('*'*80)

from random import randint
from math import sqrt

print('a) Translation from representation 1 to representation 2:')
size = randint(2,6)
rep1 = [[i, j] for i in range(size) for j in range(size)]

print('Representation 1:')
for i in range(size*size):
	print(rep1[i], end='')
	if (i+1)%size == 0:
		print()

print('Representation 2:')
for i in range(len(rep1)):
	print(i, end='\t')
	if (i+1)%sqrt(len(rep1)) == 0:
		print()

print('\nb) Translation from representation 2 to representation 1:')
size = randint(2,6)
totalsize = size*size
print('Representation 2:')
for i in range(totalsize):
	print(i, end='\t')
	if (i+1)%size == 0:
		print()

rep1 = [[i, j] for i in range(int(sqrt(totalsize))) for j in range(int(sqrt(totalsize)))]

print('Representation 1:')
for i in range(len(rep1)):
	print(rep1[i], end='')
	if (i+1)%sqrt(len(rep1)) == 0:
		print()

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
a) Translation from representation 1 to representation 2:
Representation 1:
[0, 0][0, 1][0, 2]
[1, 0][1, 1][1, 2]
[2, 0][2, 1][2, 2]
Representation 2:
0	1	2	
3	4	5	
6	7	8	

b) Translation from representation 2 to representation 1:
Representation 2:
0	1	2	3	4	5	
6	7	8	9	10	11	
12	13	14	15	16	17	
18	19	20	21	22	23	
24	25	26	27	28	29	
30	31	32	33	34	35	
Representation 1:
[0, 0][0, 1][0, 2][0, 3][0, 4][0, 5]
[1, 0][1, 1][1, 2][1, 3][1, 4][1, 5]
[2, 0][2, 1][2, 2][2, 3][2, 4][2, 5]
[3, 0][3, 1][3, 2][3, 3][3, 4][3, 5]
[4, 0][4, 1][4, 2][4, 3][4, 4][4, 5]
[5, 0][5, 1][5, 2][5, 3][5, 4][5, 5]
********************************************************************************
"""
