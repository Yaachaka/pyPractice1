"""
bhch12exrc14.py: Write a simple spell-checking program. The user should enter a string and the program should print out a list of all the words it thinks are misspelled. These would be all the words it cannot find in a wordlist.
"""
print('*'*80)

from string import punctuation
all_words = [line.strip().lower() for line in open('wordlist.txt')]
string1 = input('Enter a string: ').lower()
for i in string1:
	if i in punctuation:
		string1 = string1.replace(i, '')

str1_lst = string1.split(' ')
print('These words could not be found in the wordlist:')
for i in str1_lst:
	if i not in all_words:
		print(i, end=', ')

print()
print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter a string: Helloo there... Heww are you??
These words could not be found in the wordlist:
helloo, heww,
********************************************************************************
"""