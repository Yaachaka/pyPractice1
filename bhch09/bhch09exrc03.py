"""
bhch09exrc03.py: A good program will make sure that the data its users enter is valid. Write a program that asks the user for a weight and converts it from kilograms to pounds. Whenever the user enters a weight below 0, the program should tell them that their entry is invalid and then ask them again to enter a weight. [Hint: Use a while loop, not an if statement].
"""
print('*'*80)

wkg = eval(input('Enter weight in Kg: '))
while wkg < 0:
	
	wkg = eval(input('Invalid weight. Enter again: '))
pounds = wkg * 2.20462
print('Weight in pounds:', pounds)
print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter weight in Kg: 34
Weight in ponuds: 74.95707999999999
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter weight in Kg: -34
Invalid weight. Enter again: -45
Invalid weight. Enter again: 45
Weight in pounds: 99.2079
********************************************************************************
"""