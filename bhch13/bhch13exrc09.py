"""
bhch13exrc09.py: Write a function called factors that takes an integer and returns a list of its factors.
"""
print('*'*80)

def number_of_factors(n):
	factors = []
	for i in range(1, n):
		if not n%i:
			factors.append(i)
	return factors

n = eval(input('Enter an integer: '))
print('Factors to given number including 1 and excluding itself is {:}.'.format(number_of_factors(n)))


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter an integer: 2323
Factors to given number including 1 and excluding itself is [1, 23, 101].
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter an integer: 12321
Factors to given number including 1 and excluding itself is [1, 3, 9, 37, 111, 333, 1369, 4107].
********************************************************************************
"""