"""
bhch10exrc19.py: Write a program that repeatedly asks the user to enter a birthday in the format month/day (like 12/25 or 2/14). The user indicates they are done entering birthdays by entering done. The program should return a count of how many of those birthdays are in February and how many are on the 25th of some month (any month).
"""
print('*'*80)

months = []
days = []

not_done = 1
print('Enter birthdays in the format month/day (like 12/25 or 2/14):')
print('(When done entering all, type \'done\' and press \'Enter\')')
while not_done:
	x = input('> ')
	if x == 'done':
		break
	if not x.isalpha() and x.count('/'):
		m = x[:x.index('/')]
		d = x[x.index('/')+1:]

		if m.isdigit() and d.isdigit() and 0 < int(m) < 13 and 0 < int(d) < 32:
			months.append(int(m))
			days.append(int(d))
		else:
			print('Wrong input :(')
	else:
		print('Wrong input :(')

print('\nThere are,')
print(months.count(2), 'birthdays in february.')
print(days.count(25), 'birthdays on 25th of any given month')
print('along with others.')

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter birthdays in the format month/day (like 12/25 or 2/14):
(When done entering all, type 'done' and press 'Enter')
> 23/23
Wrong input :(
> 2/34
Wrong input :(
> 2/12
> 5/25
> 2/25
> 2-11
Wrong input :(
> done

There are,
2 birthdays in february.
2 birthdays on 25th of any given month
along with others.
********************************************************************************
"""