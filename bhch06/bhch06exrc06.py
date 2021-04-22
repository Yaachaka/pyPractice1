"""
bhch06exrc06.py 
Write a program that asks the user to enter a string s and then converts s to lowercase, removes all the periods and commas from s, and prints the resulting string.
"""
s = input('Enter your string: ')
s = s.lower()

for i in '.,':
	s = s.replace(i, '')
	
print('Formatted string:', s)