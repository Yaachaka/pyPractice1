"""
bhch08exrc02.py: Write a program that allows the user to enter five numbers (read as strings). Create a string that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2, 5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
"""
print('*'*80)

nums = input('Enter numbers: ')
l = '+'.join(''.join(nums.split(' ')).split(','))
print(l)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter numbers: 1, 2, 3, 4, 5, 6, 7
1+2+3+4+5+6+7
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter numbers: 1,2,3,4,54,5,6,6
1+2+3+4+54+5+6+6
********************************************************************************
"""