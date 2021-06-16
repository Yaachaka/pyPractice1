"""
bhch10exrc14.py: Write a program to find the smallest positive integer that satisfies the following property: If you take the leftmost digit and move it all the way to the right, the number thus obtained is exactly 3.5 times larger than the original number. For instance, if we start with 2958 and move the 2 all the way to the right, we get 9582, which is roughly 3.2 times the original number.
"""
print('*'*80)

that_int = 0
i = 20
while not that_int:
	x = str(i)
	x = x[1:] + x[0]
	y = str(int(i*3.5))
	if x == y:
		that_int = i
		break
	i += 1

print('The number is', that_int)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
The number is 153846
********************************************************************************

"""