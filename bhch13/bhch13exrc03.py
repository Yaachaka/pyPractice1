"""
bhch13exrc03.py: Write a function called sum_digits that is given an integer num and returns the sum of the digits of num.
"""
print('*'*80)

def sum_digits(num):
	num = str(num)
	sum = 0
	for i in num:
		sum += int(i)
	return sum

num = eval(input('Enter an integer: '))
print('Sum of the integers in the number is {:}.'.format(sum_digits(num)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter an integer: 234543
Sum of the integers in the number is 21.
********************************************************************************
"""