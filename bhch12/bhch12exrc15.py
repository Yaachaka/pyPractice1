"""
bhch12exrc15.py: Crossword cheater: When working on a crossword puzzle, often you will have a word where you know several of the letters, but not all of them. You can write a computer program to help you. For the program, the user should be able to input a word with the letters they know filled in and asterisks for those they don’t know. The program should print out a list of all words that fit that description. For example, the input th***ly should return all the words that could work, namely thickly and thirdly.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]
user_word = input('Enter your word: ').lower()

print('Possible words are:')
for word in all_words:
	if len(word) == len(user_word):
		for i in range(len(word)):
			if user_word[i] != '*':
				if user_word[i] != word[i]:
					break
		else:
			print(word)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter your word: hi***y
Possible words are:
highly
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter your word: t****ly
Possible words are:
totally
********************************************************************************
"""