"""
bhch12exrc17.py: Using the wordlist, produce a dictionary whose keys are the letters a through z and whose values are the percentage of words that use that letter.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]
letters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for word in all_words:
	w = ''
	for i in word:
		if i not in w:
			w += i
	for i in w:
		letters[i] += 1

print('letters and percentage of words that contain the letter:')
l = len(all_words)
for i in letters:
	print('{:} - {:6.2f}%, '.format(i, letters[i]*100/l), end='')

print()

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
letters and percentage of words that contain the letter:
a -  45.35%, b -  10.94%, c -  26.85%, d -  22.70%, e -  56.55%, f -   8.45%, g -  16.08%, h -  13.60%, i -  43.74%, j -   1.81%, k -   5.76%, l -  28.15%, m -  17.61%, n -  40.23%, o -  35.69%, p -  18.22%, q -   1.22%, r -  41.61%, s -  41.24%, t -  40.09%, u -  18.49%, v -   8.32%, w -   6.21%, x -   2.56%, y -  10.09%, z -   1.29%,
********************************************************************************
"""