"""[NOTE: Program worked for other puzzles except the given]
bhch10exrc28.py: In a magic square, each row, each column, and both diagonals add up to the same number. A partially filled magic square is shown below. Write a program to check through all the possibilities to fill in the magic square.

	5 _ _
	_ 6 2
	3 8 _
"""
print('*'*80)

from pprint import pprint

mat = [[5, 0, 0], [0, 6, 2], [3, 8, 0]]
#mat = [[4, 0, 0], [0, 5, 7], [8, 1, 0]]#[[4, 9, 2], [3, 5, 7], [8, 1, 6]] = 15
#mat = [[2, 0, 0], [0, 5, 1], [4, 3, 0]]#[[2, 7, 6], [9, 5, 1], [4, 3, 8]]

mat2 = [[mat[i][j] for j in range(len(mat[0])) ]for i in range(len(mat))]

it_count = 0
print('Given puzzle:')
pprint(mat)
print('Possible solutions:')
for i in range(1, 10):
	mat2[0][1] = i
	for j in range(1, 10):
		mat2[0][2] = j
		for k in range(1, 10):
			mat2[1][0] = k
			for l in range(1, 10):
				mat2[2][2] = l
				it_count += 1 #To keep track of number of iterations
				dp = sum([mat2[m][m] for m in range(len(mat2))]) #Principle diagonal
				ds = sum([mat2[m][2-m] for m in range(len(mat2))]) #Secondary diagonal
				if dp == ds:
					rows = [sum(mat2[m]) for m in range(len(mat2))]
					if rows.count(dp) == len(mat2):
						cols = [sum([mat2[n][m] for n in range(len(mat2))]) for m in range(len(mat2[0]))]
						if cols.count(dp) == len(mat2):
							pprint(mat2)
							print('Iteration count = {:}, Sum = {:}.'.format(it_count,dp))

print('Total number of iterations:', it_count)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Given puzzle:
[[5, 0, 0], [0, 6, 2], [3, 8, 0]]
Possible solutions:
Total number of iterations: 6561
********************************************************************************

@@@@ Trial2:
********************************************************************************
Given puzzle:
[[4, 0, 0], [0, 5, 7], [8, 1, 0]]
Possible solutions:
[[4, 9, 2], [3, 5, 7], [8, 1, 6]]
Iteration count = 5937, Sum = 15.
Total number of iterations: 6561
********************************************************************************

@@@@ Trial3:
********************************************************************************
Given puzzle:
[[2, 0, 0], [0, 5, 1], [4, 3, 0]]
Possible solutions:
[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
Iteration count = 4859, Sum = 15.
Total number of iterations: 6561
********************************************************************************
"""