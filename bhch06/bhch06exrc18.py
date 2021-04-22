"""
bhch06exrc18.py:
The goal of this exercise is to see if you can mimic the behavior of the in operator and the
count and index methods using only variables, for loops, and if statements.  
(a) Without using the in operator, write a program that asks the user for a string and a letter
and prints out whether or not the letter appears in the string.  
(b) Without using the count method, write a program that asks the user for a string and a
letter and counts how many occurrences there are of the letter in the string.  
(c) Without using the index method, write a program that asks the user for a string and
a letter and prints out the index of the first occurrence of the letter in the string. If the
letter is not in the string, the program should say so.
"""
print('*'*80)

string = input('Enter a string: ').lower()
letter = input('Enter a letter: ').lower()

letterExist = 0
letterCount = 0
letterIndex = 0

for i in range(len(string)):
	if string[i] == letter:
		letterCount = letterCount + 1
		if letterExist == 0:
			letterExist = 1
			letterIndex = i
			
if letterExist:
	print('Letter exist at index', letterIndex)
	print('No. of times the letter appeared:', letterCount)
else:
	print('Letter does not exist.')
	
print('*'*80)

"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a string: how are you
Enter a letter: o
Letter exist at index 1
No. of times the letter appeared: 2
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a string: Learning from the beginning.
Enter a letter: g
Letter exist at index 7
No. of times the letter appeared: 3
********************************************************************************
"""