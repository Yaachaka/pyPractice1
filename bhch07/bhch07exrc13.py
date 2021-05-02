"""
bhch07exrc13.py: Write a program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
"""
print('*'*80)

l = eval(input('Enter a list: '))

j = 0
for i in range(len(l)):
	if l.count(l[j]) > 1:
		del l[j]
	else:
		j = j + 1

print('Modified list:', l)
print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a list: [1,2,3,4,3,3,2,4,5,2,2,1,3]
Modified list: [4, 5, 2, 1, 3]
********************************************************************************

@@@@ Trial2: Notice the way the input entered.
********************************************************************************
Enter a list: 1,2,3,4,2,4,5,1,4,3,2
Traceback (most recent call last):
  File "bhch07/bhch07exrc13.py", line 11, in <module>
    del l[j]
TypeError: 'tuple' object doesn't support item deletion
make: *** [makefile:9: runn] Error 1
"""