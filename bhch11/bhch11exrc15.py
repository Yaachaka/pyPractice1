"""
bhch11exrc15.py: The following problem is from Chapter 6. Try it again, this time using a dictionary whose keys are the names of the time zones and whose values are offsets from the Eastern time zone.
Write a program that converts a time from one time zone to another. The user enters the time in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters is that of the original time and the second is the desired time zone. The possible time zones are Eastern, Central, Mountain, or Pacific.

	Time: 11:48pm
	Starting zone: Pacific
	Ending zone: Eastern
	2:48am
"""
print('*'*80)

print('Times zones in USA are based on Greenwich Mean Time (GMT) - 12:00pm')
print('EST --- Eastern Standard Time --- 07:00am')
print('CST --- Central Standard Time --- 06:00am')
print('MST --- Mountain Standard Time --- 05:00am')
print('PST --- Pacific Standard Time --- 04:00am')
print('AKST --- Alaska Standard Time --- 03:00am')
print('YST --- Yukon Standard Time --- 03:00am')
print('AHST --- Alaska-Hawaii Standard Time --- 02:00am')

zone_dict = {'eastern': 0, 'central': -1, 'mountain': -2, 'pacific': -3, 'alaska': -4, 'yukon': -4, 'alaksa-hawaii': -5}

time = input('\nEnter time (XX:XXxm): ').lower()
time2 = [int(time[:2]), int(time[3:5]), time[-2]]
if time2[2] != 'p':
	time2[2] = 'a'

if 60<= time2[0]*60 + time2[1] <=779:
	startZone = input('Enter a start zone: ').lower()
	if startZone in zone_dict:
		endZone = input('Enter end zone: ').lower()
		if endZone in zone_dict:
			diff = zone_dict[endZone] - zone_dict[startZone]

			print()
			#Converting to 24-hour time format for convenience
			mins = time2[1]
			if time2[2] == 'p':
				if time2[0] == 12:
					mins = time2[0] * 60 + mins
				else:
					mins = time2[0] * 60 + mins + 719
			else:
				if time2[0] != 12:
					mins = time2[0] * 60 + mins
			
			#Now let's find the time for end zone
			mins = mins + diff * 60
			if not 0 <= mins < 1440:
				mins %= 1440
			print('Time in new zone is ', end ='')
			if mins < 720:
				if mins < 60:
					print('{:}:{:}{:}m'.format('%.2d'%12, '%.2d'%mins, 'a'))
				else:
					print('{:}:{:}{:}m'.format('%.2d'%(mins//60), '%.2d'%time2[1], 'a'))
			else:
				mins = mins - 720
				if mins < 60:
					print('{:}:{:}{:}m'.format('%.2d'%12, '%.2d'%mins, 'p'))
				else:
					print('{:}:{:}{:}m'.format('%.2d'%(mins//60), '%.2d'%time2[1], 'p'))
		else:
			print('Entered zone not in the list.')
	else:
		print('Entered zone not in the list.')
else:
	print('Time entered is wrong.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Times zones in USA are based on Greenwich Mean Time (GMT) - 12:00pm
EST --- Eastern Standard Time --- 07:00am
CST --- Central Standard Time --- 06:00am
MST --- Mountain Standard Time --- 05:00am
PST --- Pacific Standard Time --- 04:00am
AKST --- Alaska Standard Time --- 03:00am
YST --- Yukon Standard Time --- 03:00am
AHST --- Alaska-Hawaii Standard Time --- 02:00am

Enter time (XX:XXxm): 12:48pm
Enter a start zone: eastern
Enter end zone: mountain

Time in new zone is 10:48am
********************************************************************************

@@@@ Trial2:
********************************************************************************
Times zones in USA are based on Greenwich Mean Time (GMT) - 12:00pm
EST --- Eastern Standard Time --- 07:00am
CST --- Central Standard Time --- 06:00am
MST --- Mountain Standard Time --- 05:00am
PST --- Pacific Standard Time --- 04:00am
AKST --- Alaska Standard Time --- 03:00am
YST --- Yukon Standard Time --- 03:00am
AHST --- Alaska-Hawaii Standard Time --- 02:00am

Enter time (XX:XXxm): 01:15pm
Enter a start zone: central
Enter end zone: eastern

Time in new zone is 02:15pm
********************************************************************************
"""