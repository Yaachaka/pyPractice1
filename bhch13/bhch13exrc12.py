"""
bhch13exrc12.py: Recall that if s is a string, then s.find('a') will find the location of the first a in s. The problem is that it does not find the location of every a. Write a function called findall that given a string and a single character, returns a list containing all of the locations of that character in the string. It should return an empty list if there are no occurrences of the character in the string.
"""
print('*'*80)

def findall(s, c):
	ind = []
	i = 0
	if c in s:
		i = s.index(c)
		ind.append(i)
	i += 1
	while i < len(s) and c in s[i:]:
		loc = s[i:].index(c)
		ind.append(ind[-1] + loc)
		i += 1 + loc
	return ind

s = input('Enter a string: ')
c = input('Enter a character to find all its indices: ')[0]

print('All the locations of the character in the string: {:}.'.format(findall(s, c)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a string: hello there
Enter a character to find all its indices: m
All the locations of the character in the string: [].
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a string: hello there
Enter a character to find all its indices: e
All the locations of the character in the string: [1, 7, 8].
********************************************************************************
"""