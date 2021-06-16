"""
bhch10exrc22.py: Write a program to find all four solutions to the following problem: If a starfruit is worth $5, a mango is worth $3, and three oranges together cost $1, how many starfruits, mangoes, and oranges, totaling 100, can be bought for $100?
"""
print('*'*80)

x = y = z = not_done = 1

for i in range(1, 99):
	for j in range(1, 99):
		for k in range(1, 99):
			if i + j + k == 5 * i + 3 * j + k/3 == 100:
				print(i, 'starfruits', j, 'mangoes', k, 'oranges')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
4 starfruits 18 mangoes 78 oranges
8 starfruits 11 mangoes 81 oranges
12 starfruits 4 mangoes 84 oranges
********************************************************************************
"""