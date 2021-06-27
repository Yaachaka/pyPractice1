"""
bhch12exrc01.py: You are given a file called class_scores.txt, where each line of the file contains a oneword username and a test score separated by spaces, like below:

	GWashington 83
	JAdams 86

Write code that scans through the file, adds 5 points to each test score, and outputs the usernames and new test scores to a new file, scores2.txt.
"""
print('*'*80)

#Make each line a an element of a list
file1 = [line.strip() for line in open("class_scores.txt")]

#Create list out of each line thus exatracted using split method.
file1 = [i.split(' ') for i in file1]

#Add 5 points to the score and then put it back as it was before.
for i in range(len(file1)):
	file1[i][1] = str(int(file1[i][1]) + 5)
	file1[i] = ' '.join(file1[i])

file2 = open("scores2.txt", 'w')
for i in file1:
	print(i, file=file2)

print('*'*80)
"""PROGRAM OUTPUT

"""