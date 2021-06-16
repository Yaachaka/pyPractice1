"""
bhch10exrc20.py: Write a program that asks the user to enter a date in the format mm/dd/yy and converts it to a more verbose format. For example, 02/04/77 should get converted into February 4, 1977.
"""
print('*'*80)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print('Enter date in the format mm/dd/yy:')
print('(When done entering all, type \'done\' and press \'Enter\')')
x = input('> ')
if not x.isalpha() and x.count('/'):
	s1 = x.index('/')
	s2 = x.index('/', s1+1)

	m = x[:s1]
	d = x[s1+1:s2]
	y = x[-2:]

	if m.isdigit() and d.isdigit() and y.isdigit() and 0 < int(m) < 13 and 0 < int(d) < 32:
		print(months[int(m)-1], ' ', d, ', ', '19'+y, sep='')
	else:
		print('Wrong input :(')
else:
	print('Wrong input :(')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter date in the format mm/dd/yy:
(When done entering all, type 'done' and press 'Enter')
> 02/04/1932
February 04, 1932
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter date in the format mm/dd/yy:
(When done entering all, type 'done' and press 'Enter')
> 2/4/32
February 4, 1932
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter date in the format mm/dd/yy:
(When done entering all, type 'done' and press 'Enter')
> 32/2/12
Wrong input :(
********************************************************************************
"""