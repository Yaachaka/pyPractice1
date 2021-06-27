"""
bhch12exrc23.py: An acronym is an abbreviation that uses the first letter of each word in a phrase. We see them everywhere. For instance, NCAA for National Collegiate Athletic Association or NBC for National Broadcasting Company. Write a program where the user enters an acronym and the program randomly selects words from a wordlist such that the words would fit the acronym. Below is some typical output generated when I ran the program:

Enter acronym: ABC
['addressed', 'better', 'common']

Enter acronym: BRIAN
['bank', 'regarding', 'intending', 'army', 'naive']
"""
print('*'*80)

from random import randint

all_words = [line.strip().lower() for line in open('wordlist.txt')]
acr = input('Enter acronym: ').lower()

a = []
for i in acr:
	while True:
		ind = randint(0, len(all_words)-1)
		w = all_words[ind]
		if w[0] ==  i:
			a.append(w) 
			break
print('-', ' '.join(a))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter acronym: nimhans
- nominations involves margaret hc affordable nec strengths
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter acronym: nimhans
- noted indicated matching henry active nominations scale
********************************************************************************
"""