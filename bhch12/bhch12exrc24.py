"""
bhch12exrc24.py: This problem is about a version of the game Jotto. The computer chooses a random five-letter word with no repeat letters. The player gets several turns to try to guess the computer’s word. On each turn, the player guesses a five-letter word and is told the number of letters that their guess has in common with the computer’s word.
"""
print('*'*80)

from random import randint

all_words = [line.strip().lower() for line in open('wordlist.txt')]

w2 = ''
while True:#To randomly select 5 letter word from wordlist that contain no repeated letters
	ind = randint(0, len(all_words)-1)
	w = all_words[ind]
	w2 = ''
	if len(w) == 5:
		for i in w:
			if i not in w2:
				w2 += i
	if len(w2) == 5:
		break

while True:
	guess = input('Guess 5 letter word: ').lower()[:5]
	count = 0
	if guess == w2:
		print('Right!!! the word is {:}.'.format(w2))
		break
	else:
		for i in w2:
			if i in guess:
				count += 1
		print('Your guess contains {:} letters in common to chosen word.'.format(count))
		q = input('Reveal the answer\t\t\ta\n'
		'Guess again\t\t\tb\n'
		'exit\t\t\tc or other character: ').lower()[0]
		if q == 'a':
			print(w2)
			break
		if q != 'b':
			break

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Guess 5 letter word: ghost
Your guess contains 1 letters in common to chosen word.
Reveal the answer                       a
Guess again                     b
exit                    c or other character: b
Guess 5 letter word: ghast
Your guess contains 2 letters in common to chosen word.
Reveal the answer                       a
Guess again                     b
exit                    c or other character: a
meals
********************************************************************************
"""