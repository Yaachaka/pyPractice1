"""
bhch06exrc13.py:
Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe.
"""
print('*'*80)

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if len(word1) == len(word2):
	for i in range(len(word1)):
		print(word1[i], word2[i], sep='', end='')
	print()
else:
	print('The words are of different length.')

print('*'*80)

"""PROGRAM OUTPUT
Trial1:
********************************************************************************
Enter a word: abcde
Enter another word: ABCDE
aAbBcCdDeE
********************************************************************************

Trial2:
********************************************************************************
Enter a word: god
Enter another word: goddess
The words are of different length.
********************************************************************************

Trial3:
********************************************************************************
Enter a word: god
Enter another word: dog
gdoodg
********************************************************************************
"""