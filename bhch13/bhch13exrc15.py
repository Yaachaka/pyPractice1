"""
bhch13exrc15.py: Write a function called root that is given a number x and an integer n and returns x^(1/n). In the function definition, set the default value of n to 2.
"""
print('*'*80)

def root(x, n=2):
	return x**(1/n)

x = eval(input('Enter value of x: '))
n = eval(input('Enter value of n: '))

print('The solution upon passing only x: {:}.'.format(root(x)))
print('The solution upon passing both x and n: {:}.'.format(root(x, n)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter value of x: 5
Enter value of n: 3
The solution upon passing only x: 2.23606797749979.
The solution upon passing both x and n: 1.7099759466766968.
********************************************************************************
"""