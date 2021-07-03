"""
bhch13exrc13.py: Write a function called change_case that given a string, returns a string with each upper case letter replaced by a lower case letter and vice-versa.
"""
print('*'*80)

def change_case(s):
	s = list(s)
	for i in range(len(s)):
		if s[i].isalpha():
			if s[i].islower():
				s[i] = s[i].upper()
			else:
				s[i] = s[i].lower()
	s = ''.join(s)
	return s

s = input('Enter a string: ')
print('The string with inverted case: {:}.'.format(change_case(s)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter a string: HelLo ThErE
The string with inverted case: hELlO tHeRe.
********************************************************************************
"""