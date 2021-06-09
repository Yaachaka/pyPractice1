"""
bhch08exrc15.py: Use a list comprehension to create the list below, which consists of ones separated by increasingly many zeroes. The last two ones in the list should be separated by ten zeroes.

	[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

"""
print('*'*80)

l = [[0]*i + [1] for i in range(11)]

k = [1] + [j for M in l for j in M]

print('l =',l)
print('k =',k)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
l = [[1], [0, 1], [0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 1]]
k = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
********************************************************************************
"""