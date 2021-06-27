"""
bhch12exrc03.py: You are given a file called logfile.txt that lists log-on and log-off times for users of a system. A typical line of the file looks like this:

	Van Rossum, 14:22, 14:37

Each line has three entries separated by commas: a username, a log-on time, and a log-off time. Times are given in 24-hour format. You may assume that all log-ons and log-offs occur within a single workday.
Write a program that scans through the file and prints out all users who were online for at least an hour.
"""
print('*'*80)

file1 = [line.strip() for line in open('logfile.txt')]
file1 = [i.split(', ') for i in file1]
print('List of users who were online atleast for an hour:')

for i in file1:
	h1 = int(i[1][:i[1].index(':')])
	m1 = int(i[1][-2:])
	h2 = int(i[2][:i[2].index(':')])
	m2 = int(i[2][-2:])
	if (h2*60 + m2) - (h1*60 + m1) > 59:
		print('-', i[0])

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
List of users who were online atleast for an hour:
- Arun Kumar
- Ravi
- Sujatha
********************************************************************************
"""