"""
bhch10exrc17.py: Write a program that repeatedly asks the user to enter a height in the format feet'inches" (like 5'11" or 6'3". The user indicates they are done entering heights by entering done. The program should return a count of how many 4-footers, 5-footers, 6-footers, and 7-footers were entered.
"""
print('*'*80)

heights = []

not_done = 1
print('Enter heights in the format feet\'inches\":')
print('(When done entering all, type \'done\' and press \'Enter\')')
while not_done:
	x = input('> ')
	if x == 'done':
		break
	ft = x[:x.index('\'')]
	if ft.isdigit():
		heights.append(int(ft))
	else:
		print('Wrong input :(')

print('\nThere are,')
print(heights.count(4), '4-footers')
print(heights.count(5), '5-footers')
print(heights.count(6), '6-footers')
print(heights.count(7), '7-footers')
print('along with others.')


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter heights in the format feet'inches":
(When done entering all, type 'done' and press 'Enter')
> 5'34"
> 4'45"
> 4.4'45"
Wrong input :(
> 4'78
> 7'63"
> done

There are,
2 4-footers
1 5-footers
0 6-footers
1 7-footers
along with others.
********************************************************************************
"""