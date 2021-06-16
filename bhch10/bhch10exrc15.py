"""
bhch10exrc15.py: Write a program to determine how many zeroes 1000! ends with.
"""
print('*'*80)

x = '1000'

n = 0
i = -1
while not int(x[i]):
	n += 1
	i -= 1

print('1000 ends with', n, 'zeroes.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
1000 ends with 3 zeroes.
********************************************************************************

"""