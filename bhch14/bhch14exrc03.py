"""
bhch14exrc03.py: Write a class called Password_manager. The class should have a list called old_passwords that holds all of the user’s past passwords. The last item of the list is the user’s current password. There should be a method called get_password that returns the current password and a method called set_password that sets the user’s password. The set_password method should only change the password if the attempted password is different from all the user’s past passwords. Finally, create a method called is_correct that receives a string and returns a boolean True or False depending on whether the string is equal to the current password or not.
"""
print('*'*80)

class Password_manager:
	def __init__(self):
		self.old_passwords = []
	
	def get_password(self):
		if len(self.old_passwords):
			return self.old_passwords[-1]
		else:
			print('You haven\'t set any password yet.')
			return -1
	
	def set_password(self):
		while True:
			p = input('Enter a password: ')
			if p not in self.old_passwords:
				self.old_passwords.append(p)
				break
			else:
				print('Can\'t set this password. You have used it before.')
	
	def is_correct(self):
		if len(self.old_passwords):
			p = input('Enter password: ')
			return p == self.old_passwords[-1]
		else:
			print('You haven\'t set any password yet.')
			return -1
	

password = Password_manager()
while True:
	choice = eval(input('Choose\n  1 to get current password\n  2 to set password\n  3 to check passord for correctness\n  otherwise to exit: '))
	if choice == 1:
		if -1 != password.get_password():
			print('The last password you used is: {:}.'.format(password.get_password()))
	elif choice == 2:
		password.set_password()
	elif choice == 3:
		p = password.is_correct()
		if -1 != p:
			print('Password is correct: {:}.'.format(p))
	else:
		break

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 1
You haven't set any password yet.
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 3
You haven't set any password yet.
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 2
Enter a password: Hello
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 1
The last password you used is: Hello.
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 3
Enter password: Hell
Password is correct: False.
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 2
Enter a password: Hello
Can't set this password. You have used it before.
Enter a password: dude
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 1
The last password you used is: dude.
Choose
  1 to get current password
  2 to set password
  3 to check passord for correctness
  otherwise to exit: 4
********************************************************************************
"""