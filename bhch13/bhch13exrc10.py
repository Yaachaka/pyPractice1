"""
bhch13exrc10.py: Write a function called closest that takes a list of numbers L and a number n and returns the largest element in L that is not larger than n. For instance, if L=[1,6,3,9,11] and n=8, then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than 8. Don’t worry about if all of the things in L are smaller than n.
"""
print('*'*80)

def closest(L, n):
	l = [i for i in L if i <= n]
	return max(l)

L = eval(input('Enter  a list: '))
n = eval(input('Enter an integer to find the largest integer in the list but not greater than n: '))

print('The solution is {:}.'.format(closest(L, n)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter  a list: [1, 34, 55, 5654, 23]
Enter an integer to find the largest integer in the list but not greater than n: 100
The solution is 55.
********************************************************************************
"""