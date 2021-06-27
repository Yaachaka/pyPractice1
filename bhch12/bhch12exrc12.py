"""
bhch12exrc12.py: Suppose we write all the words in the wordlist backwards and then arrange these backwards words alphabetically. Write a program that prints the last word in this modified wordlist.
"""
print('*'*80)

all_words = [line.strip() for line in open('wordlist.txt')]
all_words_r = [word[::-1] for word in all_words]
all_words_r.sort()

print('Last word in this modified wordlist is \'{:}\'.'.format(all_words_r[-1]))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Last word in this modified wordlist is 'zzub'.
********************************************************************************
"""