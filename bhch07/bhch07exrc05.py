"""
bhch07exrc05.py: Ask the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed.
"""
print('*'*80)

strlist = eval(input('Enter a list of strings: '))

for i in range(len(strlist)):
	strlist[i] = strlist[i][1:]

print('Formatted list of strings:')
print(strlist)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
******************************************************************************
Enter a list of strings: ['hello', 'there']
Formatted list of strings:
['ello', 'here']
********************************************************************************
@@@@ Trial2:
********************************************************************************
Enter a list of strings: ['Hello', 'there', 'how', 'are', 'you']
Formatted list of strings:
['ello', 'here', 'ow', 're', 'ou']
********************************************************************************
"""