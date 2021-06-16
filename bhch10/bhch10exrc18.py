"""
bhch10exrc18.py: Write a program that repeatedly asks the user to enter a football score in the format winning score-losing score (like 27-13 or 21-3). The user indicates they are done entering scores by entering done. The program should then output the highest score and the lowest score out of all the scores entered.
"""
print('*'*80)

high = 0
low = 999

not_done = 1
print('Enter football scores in the format winning score-losing score (like 27-13 or 21-3):')
print('(When done entering all, type \'done\' and press \'Enter\')')
while not_done:
	x = input('> ')
	if x == 'done':
		break
	if not x.isalpha() and x.count('-'):
		w = x[:x.index('-')]
		l = x[x.index('-')+1:]

		if w.isdigit() and l.isdigit() and int(l) < int(w):
			if high < int(w):
				high = int(w)
			if low > int(l):
				low = int(l)
		else:
			print('Wrong input :(')
	else:
		print('Wrong input :(')

print('\nThe highest score is', high)
print('The lowest score is', low)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter football scores in the format winning score-losing score (like 27-13 or 21-3):
(When done entering all, type 'done' and press 'Enter')
> 3-5
Wrong input :(
> 23-5
> as23-as43
Wrong input :(
> 23.34-4
Wrong input :(
> 54-34
> 3-2
> done

The highest score is 54
The lowest score is 2
********************************************************************************
"""