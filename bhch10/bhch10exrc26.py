"""
bhch10exrc26.py: Write a program that asks the user for a number and prints out all the ways to write the number as difference of two perfect squares, x^2 - y^2, where x and y are both between 1 and 1000. Writing a number as a difference of two squares leads to clever techniques for factoring large numbers.
"""
print('*'*80)

number = int(eval(input('Enter a number: ')))
for i in range(1, 1001):
	for j in range(1, 1001):
		if i**2 - j**2 == number:
			print('x^2 - y^2 = number for x = {:} and y = {:}'.format(i, j))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a number: 23
x^2 - y^2 = number for x = 12 and y = 11
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a number: 12
x^2 - y^2 = number for x = 4 and y = 2
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter a number: 99
x^2 - y^2 = number for x = 10 and y = 1
x^2 - y^2 = number for x = 18 and y = 15
x^2 - y^2 = number for x = 50 and y = 49
********************************************************************************
"""