"""
bhch09exrc10.py: Write a program that has a list of ten words, some of which have repeated letters and some which don’t. Write a program that picks a random word from the list that does not have any repeated letters.
"""
print('*'*80)

from random import randint

#list1 = ['pepper', 'spray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'import', 'settings', 'cat']
list1 = ['pepper', 'sspray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'importp', 'settings', 'catt']

print('list:', list1)

check = [0 for i in range(len(list1))]

while True:
	ind = randint(0, len(list1)-1)
	check[ind] = 1
	word = list1[ind]
	for i in word:
		if word.count(i) > 1:
			break
	else:
		print('Randomly found word with nonrepeated letters:', word)
		break
	
	if check.count(1) == 10: #Exit if all words in list are checked
		print('Every word has repeated letters.')
		break
		
print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
*******************************************************************************
list: ['pepper', 'spray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'import', 'settings', 'cat']
Randomly found word with nonrepeated letters: cat
********************************************************************************

@@@@ Trial2:
********************************************************************************
list: ['pepper', 'spray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'import', 'settings', 'cat']
Randomly found word with nonrepeated letters: import
********************************************************************************

@@@@ Trial3:
********************************************************************************
list: ['pepper', 'spray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'import', 'settings', 'cat']
Randomly found word with nonrepeated letters: import
********************************************************************************

@@@@ Trial4:
********************************************************************************
list: ['pepper', 'spray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'import', 'settings', 'cat']
Randomly found word with nonrepeated letters: spray
********************************************************************************

@@@@ Trial5:
********************************************************************************
list: ['pepper', 'sspray', 'college', 'student', 'leave', 'letter', 'different', 'matters', 'importp', 'settings', 'catt']
Every word has repeated letters.
********************************************************************************
"""