"""
bhch07exrc08.py: 
Write a program that asks the user for an integer and creates a list that consists of the factors of that integer.
"""
print('*'*80)

integer = eval(input('Enter an integer: '))
factors = []

for i in range(1, integer):
	if not integer % i:
		factors = factors + [i]

print('List of factors to the given integer:', factors)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter an integer: 20
List of factors to the given integer: [1, 2, 4, 5, 10]
********************************************************************************

@@@@ Trial2: ********************************************************************************
Enter an integer: 555
List of factors to the given integer: [1, 3, 5, 15, 37, 111, 185]
********************************************************************************
"""