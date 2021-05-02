"""
bhch07exrc07.py: Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].
"""
print('*'*80)

L = []
M = []
N = []

L = eval(input('Enter a list: '))
M = eval(input('Enter another list of same size: '))
if len(L) == len(M):
	for i in range(len(L)):
		N = N + [L[i] + M[i]]
	print('The resultant length:', N)
else:
	print('Lengths of two lists are different.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a list: [1,2,3]
Enter another list of same size: 1,2,3
The resultant length: [2, 4, 6]
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a list: 1,2,3,4
Enter another list of same size: 1,2,3
Lengths of two lists are different.
********************************************************************************
"""