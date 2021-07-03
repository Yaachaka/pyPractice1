"""
bhch13exrc08.py: Write a function called number_of_factors that takes an integer and returns how many factors the number has.
"""
print('*'*80)

def number_of_factors(n):
	count = 0
	for i in range(1, n):
		if not n%i:
			count += 1
			print(i)
	return count

n = eval(input('Enter an integer: '))
print('Number of factors including 1 and excluding itself is {:}.'.format(number_of_factors(n)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter an integer: 12132
1
2
3
4
6
9
12
18
36
337
674
1011
1348
2022
3033
4044
6066
Number of factors including 1 and excluding itself is 17.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter an integer: 2323
1
23
101
Number of factors including 1 and excluding itself is 3.
********************************************************************************
"""