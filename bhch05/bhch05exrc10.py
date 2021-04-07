"""
@@@@ Program statement:
Ask the user to enter 10 test scores. Write a program to do the following:
1. Print out the highest and lowest scores.
2. Print out the average of the scores.
3. Print out the second largest score.
4. If any of the scores is greater than 100, then after all the scores have 
been entered, print a message warning the user that a value over 100 has 
been entered.
5. Drop the two lowest scores and print out the average of the rest of them.
"""
#Get first score
print('Enter 10 scores: ')
score = eval(input())
min1 = score
min2 = score
max1 = score
max2 = score
sum1 = score
flag = 0
count = 0

if score > 100:
	flag = 1
	count = count + 1

for i in range(9):
	score = eval(input())
	if score > 100:
		flag = 1
		count = count + 1
	if max1 < score:
		max2 = max1
		max1 = score
	if min1 > score:
		min2 = min1
		min1 = score
	if max2 < score and max1 > score:
		max2 = score
	if min2 > score and min1 < score:
		min2 = score
	sum1 = sum1 + score
average = sum1/10
average2 = (sum1 - min1 - min2)/8
if flag == 1:
	print('WARNING: ', count, ' score/s greater than 100 has/have been entered.')

print('Highest among the scores: ', max1)
print('Lowest among the scores: ', min1)
print('Sum of the scores: ', sum1)
print('Average of the scores: ', average)
print('Second highest among the scores: ', max2)
print('Second lowest among the scores: ', min2)
print('Sum of the scores leaving two least numbers: ', sum1 -min1 -min2)
print('Average of the scores leaving two least scores: ', average2)