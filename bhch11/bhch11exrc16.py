"""
bhch11exrc16.py: (a) Write a program that converts Roman numerals into ordinary numbers. Here are the conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things like IV being 4 and XL being 40.
(b) Write a program that converts ordinary numbers into Roman numerals.
"""
print('*'*80)

#rom_ord = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
rom_ord = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

print('(a) Conversion from roman numerals to ordinary integers:')
r_num = input('Enter roman numeral: ').upper()

go = 1
for i in r_num:#To avoid illegal symbols in roman numeral
	if i not in 'MDCLXVI':
		go = 0
		break
for i in 'MDCLXVI':#to avoid repition of a character more than three times adjucently/contiguously
	if i*4 in r_num:
		go = 0
		break
if go:
	if len(r_num) > 1:#If there are more than one character in roman number
		r_list = []
		count = 0
		
		if r_num[:2] in rom_ord:#Check if neighbouring chars appear as in rom_ord
			r_list.append(rom_ord[r_num[:2]])
			count += 2
		else:#just append the value of first character
			r_list.append(rom_ord[r_num[0]])
			count += 1
		
		while count < len(r_num)-1:
			temp1 = r_num[count:count+2]
			if temp1 in rom_ord:#Check if neighbouring chars appear as in rom_ord
				if rom_ord[temp1] < max(r_list) or (rom_ord[r_num[count]] == max(r_list) and count == len(r_list)):#To avoid bigger valued charcter/pair to appear later in the string... For example 'MXCM'
					r_list.append(rom_ord[temp1])
					count += 2
				else:
					r_list.clear()
					break
			else:#just append the value of first character
				if rom_ord[r_num[count]] < max(r_list) or (rom_ord[r_num[count]] == max(r_list) and count == len(r_list)):
					r_list.append(rom_ord[r_num[count]])
					count += 1
				else:
					r_list.clear()
					break
			
		if sum(r_list) <= 0 or sum(r_list) > 3999:
			print('Not a valid Roman numeral.  :(')
		else:
			if len(r_num)-1 == count:
				if rom_ord[r_num[-1]] < max(r_list) or (rom_ord[r_num[-1]] == max(r_list) and count == len(r_list)):
					r_list.append(rom_ord[r_num[count]])
					print('Equivalent ordinary number is', sum(r_list))
				else:
					print('Not a valid Roman numeral.  :(')
			else:
				print('Equivalent ordinary number is', sum(r_list))
	else:#If there is only one character in roman number
		print('Equivalent ordinary number is', rom_ord[r_num])
else:
	print('Invalid characters in roman numeral/Invalid Roman numeral.')


print('\n(b) Conversion from ordinary integers to roman numeral:')
num = eval(input('Enter an integer(between 1 & 3999 inclusively): '))
if 0 < num < 4000:
	nr_list = []

	while num:
		m = 10 ** (len(str(num))-1)
		temp1 = int(str(num)[0]) * m
		if temp1:
			temp2 = 0
			for i in rom_ord:
				x = rom_ord[i]
				if x <= temp1:
					while temp2 < temp1:
						temp2 += x
						nr_list.append(i)
					if temp2 > temp1:
						temp2 -= x
						del nr_list[-1]
					if temp2 == temp1:
						break
			num -= temp1
	
	nr_num = ''.join(nr_list)
	print('Equivalent Roman number is', nr_num)
else:
	print('Idiot!!!!')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
(a) Conversion from roman numerals to ordinary integers:
Enter roman numeral: mmcmlxxxiii
Equivalent ordinary number is 2983

(b) Conversion from ordinary integers to roman numeral:
Enter an integer(between 1 & 3999 inclusively): 2983
Equivalent Roman number is MMCMLXXXIII
********************************************************************************

@@@@ Trial2:
********************************************************************************
(a) Conversion from roman numerals to ordinary integers:
Enter roman numeral: mxcmi
Not a valid Roman numeral.  :(

(b) Conversion from ordinary integers to roman numeral:
Enter an integer(between 1 & 3999 inclusively): 4002
Idiot!!!!
********************************************************************************
"""