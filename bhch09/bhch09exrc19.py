"""
bhch09exrc19.py: Randomly generate a 9 x 9 list where the entries are integers between 1 and 9 with no repeat entries in any row or in any column.
"""
print('*'*80)

from random import randint

l1 = [[0 for i in range(9)] for j in range(9)]
l1[0] = [i for i in range(1,10)] 

n_iterations = 0
for r in range(1, 9):#row
	zeroes = 1
	start = 1
	while zeroes: #while there exist atleast one zero
		for c in range(9):#column
			for i in range(start, start+9):
				n_iterations += 1
				cols = [[l1[j][k] for j in range(9)] for k in range(9)]
				if not (l1[r].count(i) or cols[c].count(i)):
					if i % 9:
						l1[r][c] = i % 9
					else:
						l1[r][c] = 9
					zeroes = l1[r].count(0)
					break

for i in range(9):
	for j in range(9):
		print(l1[i][j], end=' ')
	print()

print('Total number of iterations:', n_iterations)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
1 2 3 4 5 6 7 8 9
9 1 2 3 4 5 6 7 8
2 3 1 5 6 4 8 9 7
7 9 8 1 3 2 4 5 6
6 8 7 9 2 1 3 4 5
8 7 9 2 1 3 5 6 4
5 6 4 8 9 7 1 3 2
4 5 6 7 8 9 2 1 3
3 4 5 6 7 8 9 2 1
Total number of iterations: 1883
********************************************************************************
"""