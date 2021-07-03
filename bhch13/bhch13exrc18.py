"""
bhch13exrc18.py: Our number system is called base 10 because we have ten digits: 0, 1, . . . , 9. Some cultures, including the Mayans and Celts, used a base 20 system. In one version of this system, the 20 digits are represented by the letters A through T. Here is a table showing a few conversions:

10-20	10-20	10-20	10-20
 0-A	 8-I	16-Q	39-BT
 1-B	 9-J	17-R	40-CA
 2-C	 10-K	18-S	41-CB
 3-D	 11-L	19-T	60-DA
 4-E	 12-M	20-BA	399-TT
 5-F	 13-N	21-BB	400-BAA
 6-G	 14-O	22-BC	401-BAB
 7-H	 15-P	23-BD	402-BAC
Write a function called base20 that converts a base 10 number to base 20. It should return the result as a string of base 20 digits. One way to convert is to find the remainder when the number is divided by 20, then divide the number by 20, and repeat the process until the number is 0. The remainders are the base 20 digits in reverse order, though you have to convert them into their letter equivalents
"""
print('*'*80)

base20_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T'}

def base20(n):
	b20 = []
	if n < 20:
		return base20_dict[n]
	else:
		b20.insert(0, base20_dict[n%20])
		b20.insert(0, base20(n//20))
		return ''.join(b20)

n = eval(input('Enter an integer: '))
print('Equivalent value in base 20 is {:}.'.format(base20(n)))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter an integer: 401
Equivalent value in base 20 is BAB.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter an integer: 22
Equivalent value in base 20 is BC.
********************************************************************************
"""