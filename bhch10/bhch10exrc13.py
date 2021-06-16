"""
bhch10exrc13.py: The number 99 has the property that if we multiply its digits together and then add the sum of its digits to that, we get back to 99. That is, (9 x 9) + (9 + 9) = 99. Write a program to find all of the numbers less than 10000 with this property. (There are only nine of them.)
"""
print('*'*80)

spec_nums = []

for i in range(10, 10001):
	x = str(i)
	l1 = [int(i) for i in x]
	sum1 = sum(l1)
	prod1 = 1
	for j in l1:
		prod1 *= j
	if x == str(sum1 + prod1):
		spec_nums.append(i)

print(spec_nums)
print('No. of numbers:', len(spec_nums))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial:
********************************************************************************
[19, 29, 39, 49, 59, 69, 79, 89, 99]
No. of numbers: 9
********************************************************************************
"""