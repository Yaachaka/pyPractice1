"""
bhch09exrc07.py: Recall that, given a string s, s.index('x') returns the index of the first x in s and an error if there is no x.
(a) Write a program that asks the user for a string and a letter. Using a while loop, the program should print the index of the first occurrence of that letter and a message if the string does not contain the letter.
(b) Write the above program using a for/break loop instead of a while loop.
"""
print('*'*80)

string1 = input('Enter a string: ')
letter = input('Enter letter: ')

print('Part (a): Using while loop:')
size = len(string1)
i = 0

while i < size:
	if string1[i] == letter:
		print('The letter first occured at index', i)
		break
	i = i + 1
if i == size:
	print('The letter is not present in the string.')

print('Part (b): Using for/break loop:')
for j in range(len(string1)):
	if string1[j] == letter:
		print('The letter first occured at index', j)
		break
else:
	print('The letter is not present in the string.')


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a string: Govinda
Enter letter: h
Part (a): Using while loop:
The letter is not present in the string.
Part (b): Using for/break loop:
The letter is not present in the string.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a string: govinda
Enter letter: a
Part (a): Using while loop:
The letter first occured at index 6
Part (b): Using for/break loop:
The letter first occured at index 6
********************************************************************************
"""