"""
bhch10exrc21.py: Write a program that asks the user to enter a fraction in the form of a string like '1/2' or '8/24'. The program should reduce the fraction to lowest terms and print out the result.
"""
print('*'*80)

fraction = input('Enter a fraction: ')
if not fraction.isalpha() and fraction.count('/'):
	s1 = fraction.index('/')
	
	num = fraction[:s1]
	den = fraction[s1+1:]
	
	if num.isdigit() and den.isdigit():
		num = int(num)
		den = int(den)
		n = num
		d = den
		while d:#At the end n will contain GCD
			r = n % d
			n, d = d, r
		print('Reduced fraction: {:d}/{:d}'.format(num//n, den//n))


	else:
		print('Wrong input :(')
else:
	print('Wrong input :(')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a fraction: 8/24
Reduced fraction: 1/3
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a fraction: 1/2
Reduced fraction: 1/2
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter a fraction: 13/15
Reduced fraction: 13/15
********************************************************************************
"""