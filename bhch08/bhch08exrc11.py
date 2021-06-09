"""
bhch08exrc11.py: Section 8.3 described how to use the shuffle method to create a random anagram of a string. Use the choice method to create a random anagram of a string.
"""
print('*'*80)

from random import choice
word = input('Enter a word: ')

letter_list = list(word)

l = ''

l = [choice(letter_list) for i in range(len(word))]

anagram = ''.join(l)

print(anagram)


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
*******************************************************************************
Enter a word: hello there
rheoh hhhrr
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a word: I am not going.
t mgot gng  g.o
********************************************************************************
"""