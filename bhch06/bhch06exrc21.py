"""
bhch06exrc21.py:
An anagram of a word is a word that is created by rearranging the letters of the original.
For instance, two anagrams of idle are *deli* and *lied*. Finding anagrams that are real words is
beyond our reach until Chapter 12. Instead, write a program that asks the user for a string
and returns a random anagram of the string—in other words, a random rearrangement of the
letters of that string.
"""
print('*'*80)

word = input('Enter a word: ').lower()

vowels =''
consonants = ''
anagram = ''

for i in range(len(word)):
	if word[i] in 'aeiou':
		vowels = vowels + word[i]
	else:
		consonants = consonants + word[i]

consonants = consonants[::-1]

for i in range(20):
	if i < len(consonants):
		anagram = anagram + consonants[i]
	if i< len(vowels):
		anagram = anagram + vowels[i]
	if len(anagram) == len(word):
		break

print('Given word:', word)
print('Anagram:', anagram)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a word: govinda
Given word: govinda
Anagram: donivag
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a word: range
Given word: range
Anagram: ganer
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter a word: gamerbrain
Given word: gamerbrain
Anagram: narebarimg
********************************************************************************
"""