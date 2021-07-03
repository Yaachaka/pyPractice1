"""
bhch13exrc04.py: The digital root of a number n is obtained as follows: Add up the digits n to get a new number. Add up the digits of that to get another new number. Keep doing this until you get a number that has only one digit. That number is the digital root.
For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up the digits of 29 to get 2 + 9 = 11. We then add up the digits of 11 to get 1 + 1 = 2. Since 2 has only one digit, 2 is our digital root.
Write a function that returns the digital root of an integer n. [Note: there is a shortcut, where the digital root is equal to n mod 9, but do not use that here.]
"""
print('*'*80)

def digital_root(n):
	n = str(n)
	if len(n) == 1:
		return int(n)
	
	s = 0
	for i in n:
		s += int(i)
	return digital_root(s)

num = eval(input('Enter an integer: '))
print('The number\'s digital root is {:}.'.format(digital_root(num)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter an integer: 45893
The number's digital root is 2.
********************************************************************************
"""