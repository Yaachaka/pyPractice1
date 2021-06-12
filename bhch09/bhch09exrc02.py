"""
bhch09exrc02.py: (a) Write a program that uses a while loop (not a for loop) to read through a string and print the characters of the string one-by-one on separate lines.
(b) Modify the program above to print out every second character of the string.
"""
print('*'*80)

string1 = 'python.' 

print('Part (a):')
i = 0
while i < len(string1):
	print(string1[i])
	i = i + 1

print('Part (b):')
i = 1
while i < len(string1):
	print(string1[i])
	i = i + 2

print('*'*80)

"""PROGRAM OUTPUT
********************************************************************************
Part (a):
p
y
t
h
o
n
.
Part (b):
y
h
n
********************************************************************************
"""