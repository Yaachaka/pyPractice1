"""[Incomplete]
bhch10exrc24.py: Here is an old puzzle you can solve using brute force by using a computer program to check all the possibilities: In the calculation 43 + 57 = 207, every digit is precisely one away from its true value. What is the correct calculation?
"""
print('*'*80)

x = 43
y = 57
z = 207
xl = [43, 33, 53, 42, 44]
yl = [57, 47, 67, 56, 58]
zl = [207, 107, 307, 217, 206, 208]

for i in xl:
	for j in yl:
		if zl.count(i + j):
			print(i, '+', j, '=', k)

print('*'*80)
"""PROGRAM OUTPUT

"""
