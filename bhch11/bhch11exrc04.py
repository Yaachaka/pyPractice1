"""
bhch11exrc04.py: Write a program that uses a dictionary that contains ten user names and passwords. The program should ask the user to enter their username and password. If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid. If the password is correct, then the program should tell the user that they are now logged in to the system.
"""
print('*'*80)

credentials = {'Rama':'Raamaayana', 'Lakshmana':'Rekhe', 'Sita':'Devi', 'Bharatha':'Khanda', 'Dasharatha':'Maharaja', 'Dharmaraaya':'Agraja', 'Bheema':'Balishta', 'Arjuna':'Madhyama', 'Nakula':'Sahadeva', 'Sahadeva':'Panchama'}

username = input('Enter username(Case-sensitive): ')
if username in credentials:
	password = input('Enter password(Case-sensitive): ')
	if password == credentials[username]:
		print('You are now loggind into the system.')
	else:
		print('Password is invalid.')
else:
	print('Not a valid user of the system.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter username(Case-sensitive): bharatha
Not a valid user of the system.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter username(Case-sensitive): Bharatha
Enter password(Case-sensitive): khanda
Password is invalid.
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter username(Case-sensitive): Bharatha
Enter password(Case-sensitive): Khanda
You are now loggind into the system.
********************************************************************************
"""