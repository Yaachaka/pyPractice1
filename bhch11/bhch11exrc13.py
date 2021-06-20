"""
bhch11exrc13.py: Suppose you are given the following list of strings:

L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

Patterns like this show up in many places, including DNA sequencing. The user has a string of their own with only some letters filled in and the rest as asterisks. An example is a**a****. The user would like to know which of the strings in the list fit with their pattern. In the example just given, the matching strings are the first and fourth. One way to solve this problem is to create a dictionary whose keys are the indices in the user’s string of the non-asterisk characters and whose values are those characters. Write a program implementing this approach (or some other approach) to find the strings that match a user-entered string.
"""
print('*'*80)

L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

user_str = input('Enter your string: ').lower()
user_str_inds = []
if len(user_str) == len(L[0]):
	for i in range(len(user_str)):
		if user_str[i] != '*' and user_str[i].isalpha():
			user_str_inds.append(i)
	
	print('Possible strings are: ')
	for j in L:
		for i in user_str_inds:
			if j[i] != user_str[i]:
				break
		else:
			print(j)

else:
	print('No string of that length is available in library.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter your string: a******g
Possible strings are:
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter your string: a*****a*
Possible strings are:
aabaabac
aabacbab
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter your string: a**b**b*
Possible strings are:
aaabbcba
acababba
********************************************************************************
"""