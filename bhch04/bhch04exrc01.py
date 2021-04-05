length_cms = eval(input('Enter length in Centimeters: '))

if length_cms >= 0:
	length_inches = length_cms * 2.54
	print('Length in inches:', length_inches)
else:
	print('Warning: Negative length.')