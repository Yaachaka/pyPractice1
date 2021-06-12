"""
bhch09exrc17.py: Ask the user to enter the numerator and denominator of a fraction, and the digit they want to know. For instance, if the user enters a numerator of 1 and a denominator of 7 and wants to know the 4th digit, your program should print out 8, because 1/7 = .142856... and 8 is the 4th digit. One way to do this is to mimic the long division process you may have learned in grade school. It can be done in about five lines using the // operator at one point in the program.
"""
print('*'*80)

numerator = eval(input('Enter numerator: '))
denominator = eval(input('Enter denominator: '))

digit = eval(input('Position of digit after decimal point(max = 10): '))%11
if not digit:
	digit = 1

result = str('%.10f'%(numerator/denominator))
print('Division result:',result)
print(result[result.index('.')+digit], ' is the digit at position ', digit, '.', sep='')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter numerator: 1
Enter denominator: 7
Position of digit after decimal point(max = 10): 4
Division result: 0.1428571429
8 is the digit at position 4.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter numerator: 5
Enter denominator: 234
Position of digit after decimal point(max = 10): 5
Division result: 0.0213675214
6 is the digit at position 5.
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter numerator: 4
Enter denominator: 2
Position of digit after decimal point(max = 10): 4
Division result: 2.0000000000
0 is the digit at position 4.
********************************************************************************
"""