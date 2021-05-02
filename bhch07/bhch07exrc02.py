"""
bhch07exrc02.py: Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
"""
print('*'*80)

from random import randint

listrand20 = []

for i in range(20):
	listrand20.append(randint(1, 100))

print('(a) listrand20 =', listrand20)
print('(b) The average of the elements in the list:', sum(listrand20)/len(listrand20))
print('(c) Largest:', max(listrand20), '  Smallest:', min(listrand20))
listrand20.sort()
print('(d) Second largest:', listrand20[-2], '  Second smallest:', listrand20[1])

evens = 0
for i in listrand20:
	if not i%2:
		evens = evens + 1

print('(e) The number of even numbers in the list:', evens)
print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
(a) listrand20 = [9, 54, 97, 69, 46, 15, 48, 7, 1, 41, 23, 24, 24, 5, 47, 60, 23, 47, 63, 4]
(b) The average of the elements in the list: 35.35
(c) Largest: 97   Smallest: 1
(d) Second largest: 69   Second smallest: 4
(e) The number of even numbers in the list: 7
********************************************************************************

@@@@ Trial2:
********************************************************************************
(a) listrand20 = [48, 59, 84, 14, 38, 92, 61, 66, 9, 6, 40, 45, 79, 71, 88, 21, 26, 16, 81, 19]
(b) The average of the elements in the list: 48.15
(c) Largest: 92   Smallest: 6
(d) Second largest: 88   Second smallest: 9
(e) The number of even numbers in the list: 11
********************************************************************************
"""