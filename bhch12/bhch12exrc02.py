"""

bhch12exrc02.py: You are given a file called grades.txt, where each line of the file contains a one-word student username and three test scores separated by spaces, like below:

	GWashington 83 77 54
	JAdams 86 69 90

Write code that scans through the file and determines how many students passed all three tests.
"""
print('*'*80)

file1 = [line.strip() for line in open('grades.txt')]#Get the lines as list
file1 = [i.split(' ') for i in file1]#Split each line in required way

passed = 0
print('List of all students with theirs scores:')
print('{:12} {:4} {:4} {:4}'.format('Student name', 'Sub1', 'Sub2', 'Sub3'))
print('-'*26)
for i in file1:
	print('{:12} {:4} {:4} {:4}'.format(i[0], i[1], i[2], i[3]))
	if int(i[1]) > 44:
		if int(i[2]) > 44:
			if int(i[3]) > 44:
				passed += 1
print('-'*26)

print('With 45 being the passing score, {:} students passed in all three subjects.'.format(passed))


print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
List of all students with theirs scores:
Student name Sub1 Sub2 Sub3
--------------------------
Steve        83   77   54
Frank        24   65   76
John         66   45   76
Lilly        40   67   87
Ram          99   99   99
--------------------------
With 45 being the passing score, 3 students passed in all three subjects.
********************************************************************************
"""