"""
bhch13exrc07.py: Write a function that takes an integer n and returns a random integer with exactly n digits. For instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because that is really 93, which is a two-digit number.
"""
print('*'*80)

from random import sample

def n_digits(n):
	if n <= 0:
		return -1
	t = list('0987654321')
	k = sample(t, n)
	while(len(str(int(''.join(k)))) != n):
		k = sample(t, n)
	return int(''.join(k))

n = eval(input('Enter an integer between 1 and 9: '))%10
print('Here is the random integer of length n: {:}.'.format(n_digits(n)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter an integer between 1 and 9: 5
Here is the random integer of length n: 51387.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter an integer between 1 and 9: 4
Here is the random integer of length n: 9804.
********************************************************************************
"""