"""
bhch12exrc26.py: Write a program to cheat at the game Scrabble. The user enters a string. Your program should return a list of all the words that can be created from those seven letters.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]

user = input('Enter letters (max = 10): ').lower()[:10]

print('Possible words:')
for word in all_words:
	l1 = len(word)
	l2 = len(user)
	if l1 == l2:
		for i in word:
			if not(i in user and word.count(i) == user.count(i)):
				break
		else:
			print(word)


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter letters (max = 10): tarp
Possible words:
part
trap
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter letters (max = 10): retetl
Possible words:
letter
********************************************************************************
"""