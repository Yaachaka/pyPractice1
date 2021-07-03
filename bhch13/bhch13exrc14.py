"""
bhch13exrc14.py: Write a function called is_sorted that is given a list and returns True if the list is sorted and False otherwise.
"""
print('*'*80)

def is_sorted(L):
	l2 = L[:]
	l2.sort()
	return l2 == L

L = eval(input('Enter a list: '))
print('The list is sorted: {:}.'.format(is_sorted(L)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a list: [1, 5, 4]
The list is sorted: False.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a list: [23, 43, 78]
The list is sorted: True.
********************************************************************************
"""