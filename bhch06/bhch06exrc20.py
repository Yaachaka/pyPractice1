"""
bhch06exrc20.py:
Write a program that converts a time from one time zone to another. The user enters the time
in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters
is that of the original time and the second is the desired time zone. The possible time zones
are Eastern, Central, Mountain, or Pacific.
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

time = input('\nEnter time (XX:XXxm): ')
finalTime = time
startZone = input('Enter a start zone: ')
endZone = input('Enter end zone: ')

diff = 0

if startZone == 'Eastern' or startZone == 'EST':
	if endZone == 'Central' or endZone == 'CST':
		diff = -1
	elif endZone == 'Mountain' or endZone == 'MST':
		diff = -2
	elif endZone == 'Pacific' or endZone == 'PST':
		diff = -3
	elif endZone == 'Alaska' or endZone == 'AKST' or endZone == 'Yukon' or endZone == 'YST':
		diff = -4
	elif endZone == 'Alaska-Hawaii' or endZone == 'AHST':
		diff = -5
	else:
		print('Start zone entered is wrong.') 
		diff = 500
elif startZone == 'Central' or startZone == 'CST':
	if endZone == 'Eastern' or endZone == 'EST':
		diff = 1
	elif endZone == 'Mountain' or endZone == 'MST':
		diff = -1
	elif endZone == 'Pacific' or endZone == 'PST':
		diff = -2
	elif endZone == 'Alaska' or endZone == 'AKST' or endZone == 'Yukon' or endZone == 'YST':
		diff = -3
	elif endZone == 'Alaska-Hawaii' or endZone == 'AHST':
		diff = -4
	else:
		print('Start zone entered is wrong.') 
		diff = 500
elif startZone == 'Mountain' or startZone == 'MST':
	if endZone == 'Eastern' or endZone == 'EST':
		diff = 2
	elif endZone == 'Central' or endZone == 'CST':
		diff = 1
	elif endZone == 'Pacific' or endZone == 'PST':
		diff = -1
	elif endZone == 'Alaska' or endZone == 'AKST' or endZone == 'Yukon' or endZone == 'YST':
		diff = -2
	elif endZone == 'Alaska-Hawaii' or endZone == 'AHST':
		diff = -3
	else:
		print('Start zone entered is wrong.') 
		diff = 500
elif startZone == 'Pacific' or startZone == 'PST':
	if endZone == 'Eastern' or endZone == 'EST':
		diff = 3
	elif endZone == 'Central' or endZone == 'CST':
		diff = 2
	elif endZone == 'Mountain' or endZone == 'MST':
		diff = 1
	elif endZone == 'Alaska' or endZone == 'AKST' or endZone == 'Yukon' or endZone == 'YST':
		diff = -1
	elif endZone == 'Alaska-Hawaii' or endZone == 'AHST':
		diff = -2
	else:
		print('Start zone entered is wrong.') 
		diff = 500
elif startZone == 'Alaska' or startZone == 'AKST' or startZone == 'Yukon' or startZone == 'YST':
	if endZone == 'Eastern' or endZone == 'EST':
		diff = 4
	elif endZone == 'Central' or endZone == 'CST':
		diff = 3
	elif endZone == 'Mountain' or endZone == 'MST':
		diff = 2
	elif endZone == 'Pacific' or endZone == 'PST':
		diff = 1
	elif endZone == 'Alaska-Hawaii' or endZone == 'AHST':
		diff = -1
	else:
		print('Start zone entered is wrong.') 
		diff = 500
elif startZone == 'Alaska-Hawaii' or startZone == 'AHST':
	if endZone == 'Eastern' or endZone == 'EST':
		diff = 5
	elif endZone == 'Central' or endZone == 'CST':
		diff = 4
	elif endZone == 'Mountain' or endZone == 'MST':
		diff = 3
	elif endZone == 'Pacific' or endZone == 'PST':
		diff = 2
	elif endZone == 'Alaska' or endZone == 'AKST' or endZone == 'Yukon' or endZone == 'YST':
		diff = 1
	else:
		print('Start zone entered is wrong.') 
		diff = 500
else:
	print('Start zone entered is wrong.') 
	diff = 500

print()
if diff != 500:
	hours = (int(time[:2])%12)  #Extract time
	
	flag = 0  #flag if change from am to pm or otherway
	k = 1
	if diff < 0:
		k = -1
	for i in range(abs(diff)):
		if hours == 0:
			flag = 1
		hours = (hours + k)%12
			
	if hours == 0:
		hours = 12
	
	finalTime = str('%.2d'%hours) + time[2:5]
	if flag:
		if time[-2] == 'p':
			finalTime = finalTime + 'am'
		else:
			finalTime = finalTime + 'pm'
	else:
		finalTime = finalTime + time[-2:]
	
	print('End zone time:', finalTime)

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

Enter time (XX:XXxm): 12:00pm
Enter a start zone: CST
Enter end zone: YST

End zone time: 09:00am
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

Enter time (XX:XXxm): 12:00am
Enter a start zone: EST
Enter end zone: YST

End zone time: 08:00pm
********************************************************************************

@@@@ Trial3:
********************************************************************************
Times zones in USA are based on Greenwich Mean Time (GMT) - 12:00pm
EST --- Eastern Standard Time --- 07:00am
CST --- Central Standard Time --- 06:00am
MST --- Mountain Standard Time --- 05:00am
PST --- Pacific Standard Time --- 04:00am
AKST --- Alaska Standard Time --- 03:00am
YST --- Yukon Standard Time --- 03:00am
AHST --- Alaska-Hawaii Standard Time --- 02:00am

Enter time (XX:XXxm): 03:04pm
Enter a start zone: EST
Enter end zone: YST

End zone time: 11:04am
********************************************************************************

@@@@ Trial4:
********************************************************************************
Times zones in USA are based on Greenwich Mean Time (GMT) - 12:00pm
EST --- Eastern Standard Time --- 07:00am
CST --- Central Standard Time --- 06:00am
MST --- Mountain Standard Time --- 05:00am
PST --- Pacific Standard Time --- 04:00am
AKST --- Alaska Standard Time --- 03:00am
YST --- Yukon Standard Time --- 03:00am
AHST --- Alaska-Hawaii Standard Time --- 02:00am

Enter time (XX:XXxm): 03:04pm
Enter a start zone: CST
Enter end zone: YST

End zone time: 12:04pm
********************************************************************************
"""