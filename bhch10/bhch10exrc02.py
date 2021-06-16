"""
bhch10exrc02.py: Write a program that asks the user for a weight in kilograms. The program should convert the weight to kilograms, formatting the result to one decimal place.
"""
print('*'*80)

weight = eval(input('Enter weight in Kg: '))
print('Weight formatted to 1 decimal point: {:.1f}'.format(weight))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter weight in Kg: 34.4533
Weight formatted to 1 decimal point: 34.5
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter weight in Kg: 34
Weight formatted to 1 decimal point: 34.0
********************************************************************************
"""