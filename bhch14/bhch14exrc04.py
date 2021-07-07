"""
bhch14exrc04.py: Write a class called Time whose only field is a time in seconds. It should have a method called convert_to_minutes that returns a string of minutes and seconds formatted as in the following example: if seconds is 230, the method should return '5:50'. It should also have a method called convert_to_hours that returns a string of hours, minutes, and seconds formatted analogously to the previous method.
"""
print('*'*80)

class Time:
	def __init__(self, seconds):
		self.seconds = seconds

	def convert_to_minutes(self):
		return '{:}:{:}'.format(self.seconds//60, self.seconds%60)
	
	def convert_to_hours(self):
		h = self.seconds//3600
		m = self.seconds%3600//60
		s = self.seconds%60
		return '{:}:{:}:{:}'.format(h, m, s)

seconds = eval(input('Enter total number of seconds: '))
t1 = Time(seconds)
print('In terms of minutes:seconds: {:}'.format(t1.convert_to_minutes()))
print('In terms of hours:minutes:seconds: {:}'.format(t1.convert_to_hours()))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter total number of seconds: 9372
In terms of minutes:seconds: 156:12
In terms of hours:minutes:seconds: 2:36:12
********************************************************************************
"""