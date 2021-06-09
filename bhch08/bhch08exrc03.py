"""
bhch08exrc03.py: (a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence.
"""
print('*'*80)

sentence = input('Enter a sentence: ')
# Option (a)
l = sentence.split()
print('(a) Third word of the sentence:', l[2])
# Option (b)
l2 = [l[i] for i in range(2, len(l), 3)]
print('(b) Every third word of the sentence:', l2)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a sentence: Hello world.. How are you?
(a) Third word of the sentence: How
(b) Every third word of the sentence: ['How']
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a sentence: Hello there everyone. this is chapter 08. More with lists. this is problem 03.
(a) Third word of the sentence: everyone.
(b) Every third word of the sentence: ['everyone.', 'chapter', 'with', 'is']
********************************************************************************
"""