"""
bhch08exrc01.py: Write a program that asks the user to enter some text and then counts how many articles are in the text. Articles are the words 'a', 'an', and 'the'.
"""
print('*'*80)

sentence = input('Enter a statement: ').lower()
l = sentence.split()
a = l.count('a')
an = l.count('an')
the = l.count('the')

print(l)

print('ARTICLE\t\tCOUNTS\n', '-'*30, sep='')
print('a\t\t', a)
print('an\t\t', an)
print('the\t\t', the)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a statement: Help the poor.
['help', 'the', 'poor.']
ARTICLE         COUNTS
------------------------------
a                0
an               0
the              1
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a statement: An apple is a fruit. The patient needs it.
['an', 'apple', 'is', 'a', 'fruit.', 'the', 'patient', 'needs', 'it.']
ARTICLE         COUNTS
------------------------------
a                1
an               1
the              1
********************************************************************************
"""