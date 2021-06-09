"""
bhch08exrc21.py: Write a program that asks the user to enter a length. The program should ask them what unit the length is in and what unit they would like to convert it to. The possible units are inches, yards, miles, millimeters, centimeters, meters, and kilometers. While this can be done with 25 if statements, it is shorter and easier to add on to if you use a two-dimensional list of conversions, so please use lists for this problem.
"""
print('*'*80)

units = ['in', 'yards', 'mi', 'mm', 'cm', 'm', 'km']

length = eval(input('Enter length: '))
unit1 = input('Enter the current unit (in, yards, mi, mm, cm, m, km): ')
unit2 = input('Enter the unit to be converted to (in, yards, mi, mm, cm, m, km):')

conversions = [
	#   in,        yards,           mi,          mm,          cm,     m,          km
	[length, length*0.02778, length*0.00002, length*25.4, length*2.54, length*0.0254, length*0.00003], #in
	[length*36, length, length*0.00057, length*914.4, length*91.44, length*0.9144, length*0.00091], #yards
	[length*63360, length*1760, length, length*1609344, length*160934.4, length*1609.344, length*1.60934], #mi
	[length*0.03937, length*0.00109, length*6.2137e-7, length, length*0.1, length*0.001, length*1e-6], #mm
	[length*0.3937, length*0.01094, length*0.00001, length*10, length, length*0.01, length*0.00001], #cm
	[length*39.37008, length*1.09361, length*0.00062, length*1000, length*100, length, length*0.001], #m
	[length*39370.07874, length*1093.6133, length*0.62137, length*1000000, length*100000, length*1000, length], #km
]

if units.count(unit1) and units.count(unit2):
	index_unit1 = units.index(unit1)
	index_unit2 = units.index(unit2)

	print('Equivalent Length =', conversions[index_unit1][index_unit2], unit2)
else:
	print('Mentioned units are not available.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter length: 34.6
Enter the current unit (in, yards, mi, mm, cm, m, km): mi
Enter the unit to be converted to (in, yards, mi, mm, cm, m, km):yas
Mentioned units are not available.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter length: 34.5
Enter the current unit (in, yards, mi, mm, cm, m, km): km
Enter the unit to be converted to (in, yards, mi, mm, cm, m, km):yards
Equivalent Length = 37729.65885 yards
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter length: 36.8
Enter the current unit (in, yards, mi, mm, cm, m, km): mm
Enter the unit to be converted to (in, yards, mi, mm, cm, m, km):in
Equivalent Length = 1.4488159999999999 in
********************************************************************************"""