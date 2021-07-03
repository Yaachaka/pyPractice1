"""
bhch13exrc05.py: Write a function called first_diff that is given two strings and returns the first location in which the strings differ. If the strings are identical, it should return -1.
"""
print('*'*80)

def first_diff(str1, str2):
	if str1 == str2:
		return -1
	for i in range(len(str1)):
		if i < len(str2):# len(str1) is <= len(str2)
			if str1[i] != str2[i]:
				return i
		else:
			return i
	return len(str1)

s1 = 'hello'
s2 = 'hello'
s3 = 'hell'
s4 = 'hellooo'

print('Comparing {:} and {:} resulted in {:}.'.format(s1, s2, first_diff(s1, s2)))
print('Comparing {:} and {:} resulted in {:}.'.format(s1, s3, first_diff(s1, s3)))
print('Comparing {:} and {:} resulted in {:}.'.format(s1, s4, first_diff(s1, s4)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Comparing hello and hello resulted in -1.
Comparing hello and hell resulted in 4.
Comparing hello and hellooo resulted in 5.
********************************************************************************
"""