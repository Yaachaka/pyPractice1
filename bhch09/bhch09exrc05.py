"""
bhch09exrc05.py: Write a program that allows the user to enter any number of test scores. The user indicates they are done by entering in a negative number. Print how many of the scores are A’s (90 or above). Also print out the average.
"""
print('*'*80)

score = eval(input('Enter score: '))
count = 0
count2 = 0
summ = 0
while score >= 0:
	summ = summ + score
	count2 = count2 + 1
	if score >= 90:
		count = count + 1
	score = eval(input('Enter score: '))

print(count, 'scores are equal to or above 90.')
if count2:
	print('Average of all scores is:', summ/count2)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter score: -12
0 scores are equal to or above 90.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter score: 23
Enter score: -23
0 scores are equal to or above 90.
Average of all scores is: 23.0
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter score: 34
Enter score: 98
Enter score: 56
Enter score: 94
Enter score: 90
Enter score: 234
Enter score: -34
4 scores are equal to or above 90.
Average of all scores is: 101.0
********************************************************************************
"""