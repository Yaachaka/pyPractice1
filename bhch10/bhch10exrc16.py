"""
bhch10exrc16.py: Write a program that converts a decimal height in feet into feet and inches. For instance, an input of 4.75 feet should become 4 feet, 9 inches.
"""
print('*'*80)

height_ft = eval(input('Enter decimal height in feet: '))
print('That is equal to', int(height_ft), 'feet,', int((height_ft - int(height_ft))*12), 'inches.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter decimal height in feet: 4.75
That is equal to 4 feet, 9 inches.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter decimal height in feet: 45.34
That is equal to 45 feet, 4 inches.
********************************************************************************
"""