"""
bhch08exrc13.py: Let L be a list of strings. Write list comprehensions that create new lists from L for each of the following.
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
"""
print('*'*80)

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'ox', 'at']

la = [c[1:] for c in numbers]
lb = [len(c) for c in numbers]
lc = [c for c in numbers if len(c) > 2]

print(la)
print(lb)
print(lc)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
['ne', 'wo', 'hree', 'our', 'ive', 'ix', 'x', 't']
[3, 3, 5, 4, 4, 3, 2, 2]
['one', 'two', 'three', 'four', 'five', 'six']
********************************************************************************
"""