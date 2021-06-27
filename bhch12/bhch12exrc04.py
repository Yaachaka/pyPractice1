"""
bhch12exrc04.py: You are given a file called students.txt. A typical line in the file looks like: 
	walter melon	melon@email.msmary.edu	555-3141
There is a name, an email address, and a phone number, each separated by tabs. Write a program that reads through the file line-by-line, and for each line, capitalizes the first letter of the first and last name and adds the area code 301 to the phone number. Your program should write this to a new file called students2.txt. Here is what the first line of the new file should look like:

Walter Melon 	melon@email.msmary.edu	301-555-3141
"""
print('*'*80)

file1 = [line.strip().split('\t') for line in open('students.txt')]

for i in range(len(file1)):
	name = file1[i][0].split(' ')
	name[0] = name[0][0].upper() + name[0][1:].lower()
	name[1] = name[1][0].upper() + name[1][1:].lower()
	file1[i][0] = ' '.join(name)
	file1[i][2] = '301-' + file1[i][2]
	file1[i] = '\t'.join(file1[i])

file2 = open('students2.txt', 'w')
for i in file1:
	print(i, file=file2)

print('*'*80)
"""PROGRAM OUTPUT

"""