"""
bhch13exrc21.py: In Chapter 12, the way we checked to see if a word w was a real word was:

	if w in words:

where words was the list of words generated from a wordlist. This is unfortunately slow, but there is a faster way, called a binary search. To implement a binary search in a function, start by comparing w with the middle entry in words. If they are equal, then you are done and the function should return True. On the other hand, if w comes before the middle entry, then search the first half of the list. If it comes after the middle entry, then search the second half of the list. Then repeat the process on the appropriate half of the list and continue until the word is found or there is nothing left to search, in which case the function short return False. The < and > operators can be used to alphabetically compare two strings.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]

def binary_search(l, word):
	if len(l) < 10:
		return word in l
	half = len(l)//2
	l1 = l[:half]
	l2 = l[half:]
	if word <= l1[-1]:
		return binary_search(l1, word)
	else:
		return binary_search(l2, word)

word = input('Enter a word to see if it is in the wordlist: ').lower()
print('The word you entered is in the list: {:}.'.format(binary_search(all_words, word)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a word to see if it is in the wordlist: hello
The word you entered is in the list: True.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a word to see if it is in the wordlist: milkha
The word you entered is in the list: False.
********************************************************************************
"""