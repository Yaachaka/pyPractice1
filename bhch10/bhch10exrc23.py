"""
bhch10exrc23.py: The currency of a strange country has coins worth 7 cents and 11 cents. Write a program to determine the largest purchase price that cannot be paid using these two coins.
"""
print('*'*80)

nums = []

for i in range(15, 101):
	if i % 7 and i % 11:
		for j in range(1, 100):
			for k in range(1, 100):
				if 7 * j + 11 * k != i:
					if nums.count(i) == 0:
						nums.append(i)

print(nums)
print('With 100 cents = $1 being the highest price,', max(nums), 'is the highest price that cannot be paid using either 7 or 11 cents coins or even both together.')

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
[15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40, 41, 43, 45, 46, 47, 48, 50, 51, 52, 53, 54, 57, 58, 59, 60, 61, 62, 64, 65, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 85, 86, 87, 89, 90, 92, 93, 94, 95, 96, 97, 100]
With 100 cents = $1 being the highest price, 100 is the highest price that cannot be paid using either 7 or 11 cents coins or even both together.
********************************************************************************
"""