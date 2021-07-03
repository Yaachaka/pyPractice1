"""
bhch13exrc06.py: Write a function called binom that takes two integers n and k and returns the binomial coefficient (n k). The definition is (n k) = n!/(k!(n-k)!).
"""
print('*'*80)

#function to calculate factorial of an integer
def fact(n):
	if n <= 1:
		return 1
	return n*fact(n-1)

#function to find the binomial coefficent of given two integers
def binom(n, k):
	return fact(n)/(fact(k)*fact(n-k))

n = eval(input('Enter n: '))
k = eval(input('Enter k: '))

print('Binomial co-efficient of the given integers is {:}.'.format(binom(n, k)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter n: 6
Enter k: 5
Binomial co-efficient of the given integers is 6.0.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter n: 34
Enter k: 4
Binomial co-efficient of the given integers is 46376.0.
********************************************************************************
"""