"""
bhch10exrc11.py: Write a program that finds all pairs of six-digit palindromic numbers that are less than 20 apart. One such pair is 199991 and 200002.
"""
print('*'*80)

from pprint import pprint

pal_pairs = []
x = y = 1
for i in range(100000, 1000000):
	if str(i)[:] == str(i)[::-1]:
		y = i
		if y - x < 21:
			pal_pairs.append([x, y])
		x = y

pprint(pal_pairs) 

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial:
********************************************************************************
[[199991, 200002],
 [299992, 300003],
 [399993, 400004],
 [499994, 500005],
 [599995, 600006],
 [699996, 700007],
 [799997, 800008],
 [899998, 900009]]
********************************************************************************
"""