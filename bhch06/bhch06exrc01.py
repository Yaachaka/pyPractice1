"""
bhch06exrc01.py:
Write a program that asks the user to enter a string. The program should then print the
following:  
(a) The total number of characters in the string  
(b) The string repeated 10 times  
(c) The first character of the string (remember that string indices start at 0)  
(d) The first three characters of the string  
(e) The last three characters of the string  
(f) The string backwards  
(g) The seventh character of the string if the string is long enough and a message otherwise  
(h) The string with its first and last characters removed  
(i) The string in all caps  
(j) The string with every *a* replaced with an *e*  
(k) The string with every letter replaced by a space  
"""
string = input('Enter a string: ')

print('(a) The total number of characters in the string is ', len(string), '.', sep='')

print('(b) The string repeating 10 times: ')
for i in range(10):
	print('	',i+1, string)

print('(c) The first character of the string is', string[0])

print('(d) The first three characters of the string:', string[:3])

print('(e) The last three characters of the string:', string[-3:])

print('(f) String in backwards:', string[::-1])

print('(g) Seventh character if it exist:')
if '' != string[6]:
	print('	The seventh chaacter is', string[6])
else:
	print('	The string is not large enough')

print('(h) The string with its first and last characters removed:', string[1:-1])

print('(i) The string in all caps:', string.upper())

print('(j) The string with every *a* replaced with an *e*:', string.replace('a', 'e'))

print('(k) The string with every letter replaced by a space:', string.replace(string, len(string)*' '), 'Afterspace')