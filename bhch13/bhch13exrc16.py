"""
bhch13exrc16.py: Write a function called one_away that takes two strings and returns True if the strings are of the same length and differ in exactly one letter, like bike/hike or water/wafer.
"""
print('*'*80)

def one_away(s1, s2):
	count = 0
	if len(s1) == len(s2):
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				count += 1
			if count > 1:
				break
	return count == 1

s1 = input('Enter first string: ').lower()
s2 = input('Enter second string: ').lower()

print('The strings are of the same length and differ in exactly one letter: {:}.'.format(one_away(s1, s2)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter first string: letter
Enter second string: beter
The strings are of the same length and differ in exactly one letter: False.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter first string: letter
Enter second string: better
The strings are of the same length and differ in exactly one letter: True.
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter first string: letter
Enter second string: befter
The strings are of the same length and differ in exactly one letter: False.
********************************************************************************
"""