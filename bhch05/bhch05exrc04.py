"""
@@@@ Program satement:
Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.
"""
sum = 0
minus = -1
for i in range(1,2001):
	minus = minus * -1
	sum = sum + i * minus

print('SUM =',sum)