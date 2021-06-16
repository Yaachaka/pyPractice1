"""
bhch10exrc10.py: Adding certain numbers to their reversals sometimes produces a palindromic number. For instance, 241 + 142 = 383. Sometimes, we have to repeat the process. For instance, 84 + 48 = 132 and 132 + 231 = 363. Write a program that finds both two-digit numbers for which this process must be repeated more than 20 times to obtain a palindromic number.
"""
print('*'*80)

palindrome = []
for i in range(11, 100):
	pal = i
	for j in range(20):
		x = str(pal)
		if x[:] == x[::-1]:
			palindrome.append(pal)
		x = str(pal)
		pal = int(x[:]) + int(x[::-1])
	
palindrome = list(set(palindrome))
palindrome.sort()
print(palindrome)

print('*'*80)
"""PROGRAM OUTPUT

@@@@ Trial:
********************************************************************************
[11, 22, 33, 44, 55, 66, 77, 88, 99, 121, 242, 363, 484, 1111, 2222, 4444, 4884, 8888, 44044, 79497, 88088, 661166, 3654563, 44177144, 8836886388]
********************************************************************************
"""