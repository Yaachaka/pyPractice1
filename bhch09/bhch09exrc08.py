"""
bhch09exrc08.py: The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by. For instance, gcd(18, 42) is 6 because the largest number that both 18 and 42 are divisible by is 6. Write a program that asks the user for two numbers and computes their gcd. Shown below is a way to compute the GCD, called Euclid’s Algorithm.

- First compute the remainder of dividing the larger number by the smaller number.
- Next, replace the larger number with the smaller number and the smaller number with the remainder.
- Repeat this process until the smaller number is 0. The GCD is the last value of the larger number.
"""
print('*'*80)

number1 = abs(eval(input('Enter a positive integer: ')))
number2 = abs(eval(input('Enter a positive integer: ')))

large = number1
small = number2

if number1 and number2: #check for null value
	if number2 > number1:
		large = number2
		small = number1

remainder = 0
while small:
	remainder = large % small
	large = small
	small = remainder

print('GCD of the given two numbers is', large)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
*******************************************************************************
Enter a positive integer: 81
Enter a positive integer: 9
GCD of the given two numbers is 9
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a positive integer: 18
Enter a positive integer: 42
GCD of the given two numbers is 6
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter a positive integer: 13
Enter a positive integer: 146
GCD of the given two numbers is 1
********************************************************************************
"""