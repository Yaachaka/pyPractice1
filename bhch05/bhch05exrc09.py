"""
@@@@ Program Statement:
Write a program to count how many integers from 1 to 1000 are not 
perfect squares, perfect cubes, or perfect fifth powers.
"""
count1 = 0
count2 = 0
count3 = 0
for i in range(1, 1001):
	#Perfect squares
	limit1 = i**2
	if limit1 <= 1000:
		count1 = count1 + 1
	else:
		i = 1001  #stop for loop
	#Perfect cubes
	limit2 = i**3
	if limit2 <= 1000:
		count2 = count2 + 1
	#perfect fifth powers
	limit3 = i**5
	if limit3 <= 1000:
		count3 = count3 + 1

print('No. of non-perfect squares less than 1001 is ', 1000 - count1)
print('No. of non-perfect cubes less than 1001 is ', 1000 - count2)
print('No. of non-perfect fifth powers less than 1001 is ', 1000 - count3)