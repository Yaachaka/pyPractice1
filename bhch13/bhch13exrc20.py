"""
bhch13exrc20.py: Write a function called merge that takes two already sorted lists of possibly different lengths, and merges them into a single sorted list.
(a) Do this using the sort method. (b) Do this without using the sort method.
"""
print('*'*80)

def merge(l1, l2):
	l3 = l1 + l2#l3 for sorting using inbuilt sort method.
	l4 = l3[:]#l4 for sorting without using inbuilt sort method.
	l3.sort()
	print('(a) Using sort method:')
	print(l3)
	print('(b) Without using sort method:')
	l3 = []
	while len(l4):
		i = l4.index(min(l4))
		l3.append(l4[i])
		del l4[i]
	print(l3)

l1 = eval(input('Enter first list of integers: '))
l1.sort()
l2 = eval(input('Enter second list of integers: '))
l2.sort()

print('l1: {:}'.format(l1))
print('l2: {:}'.format(l2))
print('Combined sorted list: ')
merge(l1, l2)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter first list of integers: [2,45,234,23,12,56]
Enter second list of integers: [56,34,12,7,34]
l1: [2, 12, 23, 45, 56, 234]
l2: [7, 12, 34, 34, 56]
Combined sorted list:
(a) Using sort method:
[2, 7, 12, 12, 23, 34, 34, 45, 56, 56, 234]
(b) Without using sort method:
[2, 7, 12, 12, 23, 34, 34, 45, 56, 56, 234]
********************************************************************************
"""