"""
bhch06exrc08.py
At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with @prof.college.edu. Write a program that first asks the
user how many email addresses they will be entering, and then as the user enter those addresses. After all the email addresses are entered, the program should print out a message
indicating either that all the addresses are student addresses or that there were some professor addresses entered.
"""
print('*'*80)
nemails = eval(input('How many email addresses do you want to enter?: '))

nstuds = 0
nprofs = 0

for i in range(nemails):
	string = input('Enter email address: ')
	if string[-13] == 't':
		nstuds = nstuds + 1
	elif string[-13] == 'f':
		nprofs = nprofs + 1

print('Out of', nemails, ',')
print('	', nstuds, 'are students\'')
print('	', nprofs, 'are professors\'.')
print('*'*80)


"""PROGRAM OUTPUTS
@@@@ Trial1:
********************************************************************************
How many email addresses do you want to enter?: 5
Enter email address: govind@student.college.edu
Enter email address: subhash@prof.college.edu
Enter email address: peter@student.college.edu
Enter email address: shanti@prof.college.edu
Enter email address: roopesh@prof.college.edu
Out of 5 ,
         2 are students'
         3 are professors'.
********************************************************************************
"""