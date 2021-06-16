"""
bhch10exrc25.py: Write a program that finds all integer solutions to Pell’s equation x^2 - 2y^2 = 1, where x and y are between 1 and 100.
"""
print('*'*80)

for x in range(1, 101):
	for y in range(1, 101):
		if x**2 - 2*y**2 == 1:
			print('x = {:}, y = {:}'. format(x, y) )

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
x = 3, y = 2
x = 17, y = 12
x = 99, y = 70
********************************************************************************
"""