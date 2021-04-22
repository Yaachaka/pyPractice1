"""
bhch06exrc12.py:
Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.
"""
print('*'*80)

word = input('Enter a word: ')

for i in range(len(word)):
	if i%2:
		print(word[i].upper(), end='')
	else:
		print(word[i], end='')

print()
print('*'*80)

"""PROGRAM OUTPUT
Trial1:
********************************************************************************
Enter a word: rhinoceros
rHiNoCeRoS
********************************************************************************
"""