"""
bhch11exrc03.py: For this problem, use the dictionary from the beginning of this chapter whose keys are month names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month.
(e) Modify the program from part (a) and the dictionary so that the user does not have to know how to spell the month name exactly. That is, all they have to do is spell the first three letters of the month name correctly.
"""
print('*'*80)


days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

d  = input('a) Enter month name to know the number of days in it: ')
d = d[0].upper() + d[1:].lower()
if d in days:
	print('No. of days in the entered month is {:}.'.format(days[d]))
else:
	print('Month you entered doesn\'t exist.')

print('\nb) All the keys in alphabetical order:')
k = [i for i in days]# k = list(days)
k.sort()
print(k)

print('\nc) All the months with 31 days:')
d31 = [i for i in days if days[i] == 31]
print(d31)

print('\nd) Key-value pairs sorted by number of days:')
pairs = [(days[i], i) for i in days]
pairs.sort()
print(pairs)

d  = input('\ne) Enter month name to know the number of days in it: ')
d = d[0].upper() + d[1:3]
for d1 in days:
	if d in d1:
		print('No. of days in the month {:} is {:}.'.format(d1, days[d1]))
		break
else:
	print('Month you entered doesn\'t exist.')

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
a) Enter month name to know the number of days in it: july
No. of days in the entered month is 31.

b) All the keys in alphabetical order:
['April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November', 'October', 'September']

c) All the months with 31 days:
['January', 'March', 'May', 'July', 'August', 'October', 'December']

d) Key-value pairs sorted by number of days:
[(28, 'February'), (30, 'April'), (30, 'June'), (30, 'November'), (30, 'September'), (31, 'August'), (31, 'December'), (31, 'January'), (31, 'July'), (31, 'March'), (31, 'May'), (31, 'October')]

e) Enter month name to know the number of days in it: novacorp
No. of days in the month November is 30.
********************************************************************************

@@@@ Trial2:
********************************************************************************
a) Enter month name to know the number of days in it: asd
Month you entered doesn't exist.

b) All the keys in alphabetical order:
['April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November', 'October', 'September']

c) All the months with 31 days:
['January', 'March', 'May', 'July', 'August', 'October', 'December']

d) Key-value pairs sorted by number of days:
[(28, 'February'), (30, 'April'), (30, 'June'), (30, 'November'), (30, 'September'), (31, 'August'), (31, 'December'), (31, 'January'), (31, 'July'), (31, 'March'), (31, 'May'), (31, 'October')]

e) Enter month name to know the number of days in it: janagana
No. of days in the month January is 31.
********************************************************************************
"""