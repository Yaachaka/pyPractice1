"""
bhch13exrc02.py: (a) Write a function called add_excitement that takes a list of strings and adds an exclamation point (!) to the end of each string in the list. The program should modify the original list and not return anything.
(b) Write the same function except that it should not modify the original list and should instead return a new list.
"""
print('*'*80)

def add_excitement(l):
	for i in range(len(l)):
		l[i] += '!'

def add_excitement2(l):
	l2 = l[:]
	for i in range(len(l2)):
		l2[i] += '!'
	return l2

l = ['Hello', 'there', 'how', 'are', 'you']
print('(a)Before function call:\n', l)
add_excitement(l)
print('(a)After function call:\n', l)

print('(b))Before function call:\n', l)
l2 = add_excitement2(l)
print('(b)After function call:\n', l2)
print('(b)l After function call:\n', l)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
(a)Before function call:
 ['Hello', 'there', 'how', 'are', 'you']
(a)After function call:
 ['Hello!', 'there!', 'how!', 'are!', 'you!']
(b))Before function call:
 ['Hello!', 'there!', 'how!', 'are!', 'you!']
(b)After function call:
 ['Hello!!', 'there!!', 'how!!', 'are!!', 'you!!']
(b)l After function call:
 ['Hello!', 'there!', 'how!', 'are!', 'you!']
********************************************************************************
"""