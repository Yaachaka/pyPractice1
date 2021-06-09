"""
bhch08exrc12.py: Write a program that gets a string from the user containing a potential telephone number. The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. A phone number is considered valid as long as it is written in the form abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct. Test your program with the output shown below.

Enter a phone number: 1-301-447-5820
Valid
Enter a phone number: 301-447-5820
Valid
Enter a phone number: 301-4477-5820
Invalid
Enter a phone number: 3X1-447-5820
Invalid
Enter a phone number: 3014475820
Invalid
"""
print('*'*80)

flag = 0
number = input('Enter a phone number: ')
length = len(number)

if length == 12 or length == 14:
	if (number.replace('-', '')).isdigit():
		c = number.count('-')
		if c == 3 and length == 14:
			if not (number[-5] == number[-9] == number[-13] == '-'):
				flag = 1
		elif c == 2 and length == 12:
			if not (number[-5] == number[-9] == '-'):
				flag = 1
		else:
			flag = 1
	else:
		flag = 1
else:
	flag = 1

if flag:
	print('Invalid')
else:
	print('Valid')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a phone number: 3014475820
Invalid
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a phone number: 3x1-447-5820
Invalid
********************************************************************************

@@@@ Trial3:
*******************************************************************************
Enter a phone number: 301-447-5820
Valid
********************************************************************************

@@@@ Trial4:
********************************************************************************
Enter a phone number: 301-4477-5820
Invalid
********************************************************************************

@@@@ Trial5:
********************************************************************************
Enter a phone number: 1-301-447-5820
Valid
********************************************************************************"""