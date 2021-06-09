"""
bhch08exrc10.py: Write a censoring program. Allow the user to enter some text and your program should print out the text with all the curse words starred out. The number of stars should match the length of the curse word. For the purposes of this program, just use the “curse” words darn, dang, freakin, heck, and shoot. Sample output is below:

Enter some text: Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.
Oh *****, I thought I had the **** problem figured out. **** it. Oh well, it was a **** of a ****** try.
"""
print('*'*80)

from string import punctuation

curse = ['darn', 'dang', 'freakin', 'heck', 'shoot']

st1 = input('Enter a statement: ')
lenst1 = len(st1)

for c in curse:
	if c in st1.lower():
		st1 = st1.replace(c, '*'*len(c))
	
print(st1)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a statement: I am a shooter. Oh shoot
I am a *****er. Oh *****
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a statement: Oh shoot, I thought I had a dang problem figured out. Darn it. Oh well, it was a heck of a freaking try.
Oh *****, I thought I had a **** problem figured out. Darn it. Oh well, it was a **** of a *******g try.
********************************************************************************
"""