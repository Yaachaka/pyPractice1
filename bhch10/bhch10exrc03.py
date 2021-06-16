"""
bhch10exrc03.py: Write a program that asks the user to enter a word. Rearrange all the letters of the word in alphabetical order and print out the resulting word. For example, abracadabra should become aaaaabbcdrr.
"""
print('*'*80)

word = input('Enter a word: ')
l1 = list(word)

for i in range(len(l1)-1):
	for j in range(i+1, len(l1)):
		if l1[i].lower() > l1[j].lower():
			l1[i], l1[j] = l1[j], l1[i]
	
print(''.join(l1))


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a word: abracadabra
aaaaabbcdrr
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a word: Diamond
aDdimno
********************************************************************************
"""
