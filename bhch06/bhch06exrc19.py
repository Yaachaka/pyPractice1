"""
bhch06exrc19.py:
Write a program that asks the user for a large integer and inserts commas into it according
to the standard American convention for commas in large numbers. For instance, if the user
enters 1000000, the output should be 1,000,000.
"""
print('*'*80)

string = input('Enter a large integer: ')

for i in range(len(string)-3,0,-3):
	string = string[:i] + ',' + string[i:]
	
print('Formatted string:', string)
print('*'*80)

"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a large integer: 1234577555
Formatted string: 1,234,577,555
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a large integer: 334565544
Formatted string: 334,565,544
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter a large integer: 486783993772
Formatted string: 486,783,993,772
********************************************************************************
"""