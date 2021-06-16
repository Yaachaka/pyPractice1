"""
bhch10exrc31.py: Given two dates entered as strings in the form mm/dd/yyyy where the years are between 1901 and 2099, determine how many days apart they are. Here is a bit of information that may be useful: Leap years between 1901 and 2099 occur exactly every four years, starting at 1904. February has 28 days, 29 during a leap year. November, April, June, and September each have 30 days. The other months have 31 days.
"""
print('*'*80)

print('Note:\n\tYears can be between 1901 and 2099 inclusively.')
print('\tFormat should be mm/dd/yyyy.')

message = 'Wrong input. Good bye!!'
days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#non-leap year
days2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#leap year

dates = [[0,0,0,0], [0,0,0,0]]
tdays = 0
done_count = 0
for i in range(2):
	date = input('Enter date{:}: '.format(i+1))
	if len(date) == 10 and date.count('/') == 2:
		#extract date and check for correctness
		dm = int(date[:2])
		dd = int(date[3:5])
		dy = int(date[6:])

		if 1900 < dy < 2100 and 0 < dm < 13 and 0 < dd < 32:
			if dy % 4: #If not leap year
				if dd <= days1[dm - 1]:
					tdays = sum(days1[:dm-1]) + dd
					dates[i] = [dm, dd, dy, tdays]
					done_count += 1
				else:
					print(message)
					break
			else: #if leap year
				if dm == 2 and dd < 29: #if february
					tdays = sum(days2[:dm-1]) + dd
					dates[i] = [dm, dd, dy, tdays]
					done_count += 1
				elif dd <= days2[dm - 1]:
					tdays = sum(days2[:dm-1]) + dd
					dates[i] = [dm, dd, dy, tdays]
					done_count += 1
				else:
					print(message)
					break
		else:
			print(message)
			break
	else:
		print(message)
		break

if done_count == 2:
	if dates[0][2] < dates[1][2]: #year not equal
		dates[0], dates[1] = dates[1], dates[0]
	if dates[0][2] == dates[1][2]: #years equal but
		if dates[0][0] < dates[1][0]: #months not equal
			dates[0], dates[1] = dates[1], dates[0]
		if dates[0][0] == dates[1][0]: #Years equal and months equal
			if dates[0][1] < dates[1][1]: #Days equal
				dates[0], dates[1] = dates[1], dates[0]
	#dates[0] will contain the bigger date
	leaps = count = 0
	for i in range(dates[1][2] + 1, dates[0][2]):
		count += 1
		if not i % 4:
			leaps += 1

	print(dates)
	days = count * 365 + leaps
	if count:
		days += 365 - dates[1][3] + dates[0][3]
		if not (dates[1][2] % 4) and dates[1][0] >= 2:
			days += 1
	else:
		days = dates[0][3] - dates[1][3]
	
	print('It is about {:} days.'.format(days))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 04/23/1945
Enter date2: 05/21/2021
[[5, 21, 2021, 141], [4, 23, 1945, 113]]
It is about 27787 days.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 04/23/1948
Enter date2: 05/21/2021
[[5, 21, 2021, 141], [4, 23, 1948, 114]]
It is about 26691 days.
********************************************************************************

@@@@ Trial3:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 04/23/1996
Enter date2: 02/02/1996
[[4, 23, 1996, 114], [2, 2, 1996, 33]]
It is about 81 days.
********************************************************************************

@@@@ Trial4:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 02/23/1996
Enter date2: 02/02/1996
[[2, 23, 1996, 54], [2, 2, 1996, 33]]
It is about 21 days.
********************************************************************************

@@@@ Trial5:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 02/02/1995
Enter date2: 02/02/1995
[[2, 2, 1995, 33], [2, 2, 1995, 33]]
It is about 0 days.
********************************************************************************

@@@@ Trial6:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 02/30/1996
Wrong input. Good bye!!
********************************************************************************

@@@@ Trial7:
********************************************************************************
Note:
        Years can be between 1901 and 2099 inclusively.
        Format should be mm/dd/yyyy.
Enter date1: 02/29/1991
Wrong input. Good bye!!
********************************************************************************
"""