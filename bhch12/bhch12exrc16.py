"""
bhch12exrc16.py: Ask the user to enter several letters. Then find all the words that can be made with those letters, repeats allowed.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]
letters = input('Enter letters: ').lower()

print('Possible words:')
for word in all_words:
	check = 1
	for i in word:
		if i not in letters:
			check = 0
			break
	if check:
		for i in letters:
			if i not in word:
				check = 0
				break
	if check:
		print(word)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter letters: hjds
Possible words:
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter letters: lkn
Possible words:
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter letters: bly
Possible words:
********************************************************************************

@@@@ Trial4:
********************************************************************************
Enter letters: hlloe
Possible words:
hello
hole
********************************************************************************

@@@@ Trial5:
********************************************************************************
Enter letters: aekm
Possible words:
make
********************************************************************************

@@@@ Trial6:
********************************************************************************
Enter letters: eltrs
Possible words:
letters
********************************************************************************
"""