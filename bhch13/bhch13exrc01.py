"""
bhch13exrc01.py: Write a function called rectangle that takes two integers m and n as arguments and prints out an mxn box consisting of asterisks. Shown below is the output of rectangle(2,4)

	****
	****
"""
print('*'*80)

def rectangle(m, n):
	for i in range(m):
		for j in range(n):
			print('* ', end='')
		print()

rectangle(4, 5)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
* * * * *
* * * * *
* * * * *
* * * * *
********************************************************************************
"""