hour = eval(input('Enter hour: '))
am_pm = 1
am_pm = eval(input('Enter 2 for PM, default is AM: '))
ahead = eval(input('How many hours ahead?: '))
print('New hour is ', end='')

temp = hour + ahead

if am_pm == 2:
	if temp < 12:
		print(temp, 'pm')
	elif temp == 12:
		if hour == 12:
			print(temp, 'pm')
		else:
			print(temp, 'am')
	else:
		print(temp % 12, 'am')
else:
	if temp < 12:
		print(temp, 'am')
	elif temp == 12:
		if hour == 12:
			print(temp, 'am')
		else:
			print(temp, 'pm')
	else:
		print(temp % 12, 'pm')