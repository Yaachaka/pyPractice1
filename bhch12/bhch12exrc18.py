"""
bhch12exrc18.py: Using the wordlist, produce a dictionary whose keys are the letters a through z and whose values are the percentage of total letters in the wordlist that are that letter.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]
letters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for word in all_words:
	for i in word:
		letters[i] += 1

print('letters and percentage of appearance of that letter in the wordlist:')
l = len(all_words)
for i in letters:
	print('{:} - {:6.2f}%, '.format(i, letters[i]*100/l), end='')

print()

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
letters and percentage of appearance of that letter in the wordlist:
a -  53.80%, b -  11.44%, c -  30.25%, d -  25.07%, e -  76.01%, f -   9.28%, g -  17.17%, h -  14.30%, i -  54.62%, j -   1.83%, k -   5.93%, l -  32.32%, m -  19.12%, n -  48.21%, o -  42.51%, p -  20.27%, q -   1.23%, r -  48.59%, s -  50.84%, t -  47.60%, u -  19.39%, v -   8.49%, w -   6.32%, x -   2.64%, y -  10.27%, z -   1.36%,
********************************************************************************
"""