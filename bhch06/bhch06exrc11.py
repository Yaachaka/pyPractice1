"""
bhch06exrc11.py):**  
Write a program that asks the user to enter a word that contains the letter a. The program
should then print the following two lines: On the first line should be the part of the string up
to and including the the first a, and on the second line should be the rest of the string. Sample
output is shown below:
	Enter a word: buffalo  
	buffa  
	lo
"""
print('*'*80)

word = input('Enter a word: ')

position = word.index('a')

print(word[:position+1])
print(word[position+1:])

print('*'*80)


"""PROGRAM OUTPUT
Trial1:
********************************************************************************
Enter a word: david
da
vid
********************************************************************************

Trial2:
********************************************************************************
Enter a word: Govinda
Govinda

********************************************************************************
"""