"""
bhch13exrc11.py: Write a function called matches that takes two strings as arguments and returns how many matches there are between the strings. A match is where the two strings have the same character at the same index. For instance, 'python' and 'path' match in the first, third, and fourth characters, so the function should return 3.
"""
print('*'*80)

def matches(s1, s2):
	n = len(s1)
	if len(s2)< n:
		n = len(s2)
	count = 0
	for i in range(n):
		if s1[i] == s2[i]:
			count += 1
	return count
	
s1 = input('Enter string1: ')
s2 = input('Enter string2: ')

print('The number of matches is {:}.'.format(matches(s1, s2)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter string1: hello there
Enter string2: how are you?
The number of matches is 1.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter string1: python
Enter string2: path
The number of matches is 3.
********************************************************************************
"""