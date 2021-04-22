"""
bhch06exrc07.py
Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
"""
string = input('Enter a string: ').lower()

l = len(string)
if l%2:  #odd numbered length of string.
	l = len(string)//2
else:  #even numbered length of string.
	l = len(string)//2-1

if string[:len(string)//2] == string[:l:-1]:
	print('The string is a palindrome.')
else:
	print('The string is not a palindrome.')