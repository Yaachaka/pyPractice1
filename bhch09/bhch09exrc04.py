"""
bhch09exrc04.py: Write a program that asks the user to enter a password. If the user enters the right password, the program should tell them they are logged in to the system. Otherwise, the program should ask them to reenter the password. The user should only get five tries to enter the password, after which point the program should tell them that they are kicked off of the system.
"""
print('*'*80)

password = 'pythoN'
userpass = input('Enter password: ')

i = 4
while i:
	if userpass == password:
		print('You are successfully logged in.')
		break
	print('Incorrect password.', i, 'attempts left.')
	userpass = input('Enter password: ')
	i = i-1
else:
	print('You are kicked off of the system.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter password: pyto
Incorrect password. 4 attempts left.
Enter password: ghire
Incorrect password. 3 attempts left.
Enter password: sadd
Incorrect password. 2 attempts left.
Enter password: asdsf
Incorrect password. 1 attempts left.
Enter password: fdgf
You are kicked off of the system.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter password: pythoN
You are successfully logged in.
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter password: pthh
Incorrect password. 4 attempts left.
Enter password: sfdds
Incorrect password. 3 attempts left.
Enter password: pythoN
You are successfully logged in.
********************************************************************************
"""