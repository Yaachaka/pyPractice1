"""
bhch12exrc11.py: Write a program to help with word games. The user enters a word and the program uses the wordlist to determine if the user’s word is a real word or not.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]
word = input("Enter a word: ").lower()
if word in all_words:
	print('The word is in the list.')
else:
	print('The word is not in the list.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a word: ajeeb
The word is not in the list.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a word: success
The word is in the list.
********************************************************************************
"""