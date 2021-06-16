"""
bhch10exrc09.py: Write a program to determine how many of the numbers between 1 and 10000 contain the digit 3.
"""
print('*'*80)

print('Number of times the digit 3 appeared in the range 1 to 10000: ', sum([str(i).count('3') for i in range(1, 10000)]))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial:
********************************************************************************
Number of times the digit 3 appeared in the range 1 to 10000:  4000
********************************************************************************
"""