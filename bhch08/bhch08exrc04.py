"""
bhch08exrc04.py: (a) Write a program that asks the user to enter a sentence and then randomly rearranges the words of the sentence. Don’t worry about getting punctuation or capitalization correct.
(b) Do the above problem, but now make sure that the sentence starts with a capital, that the original first word is not capitalized if it comes in the middle of the sentence, and that the period is in the right place.
"""
print('*'*80)

from random import shuffle
from string import punctuation

# (a)
sentence = input('Enter a sentence: ')
l = sentence.split()
shuffle(l)
print('(a):', l)

# (b)
punct = ''
sen2 = ''
#If there is a punctuation mark to the sentence at the end.
if sentence[-1] in punctuation:
	punct = sentence[-1]
	sen2 = sentence[0].lower() + sentence[1:-1]
else:
	sen2 = sentence[0].lower() + sentence[1:]

l2 = sen2.split()
shuffle(l2)
print('(b):\nl2:', l2)
sen2 = ' '.join(l2) + punct
sen2 = sen2[0].upper() + sen2[1:]
print('Sentence:', sen2)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter a sentence: Hello there. How are you?
(a): ['Hello', 'there.', 'How', 'are', 'you?']
(b):
l2: ['you', 'there.', 'hello', 'How', 'are']
Sentence: You there. hello How are?
********************************************************************************
"""