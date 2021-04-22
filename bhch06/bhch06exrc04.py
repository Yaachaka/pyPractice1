"""
bhch06exrc04.py
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
"""
string = input('Enter a word: ')

flag = 0

for t in "aeiouAEIOU":
	if t in string:
		flag = 1
		
if flag:
	print('The program contains vowels.')
else:
	print('The program does not contain vowels.')
		