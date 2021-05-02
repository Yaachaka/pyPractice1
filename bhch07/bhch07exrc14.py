"""
bhch07exrc14.py: Write a program that asks the user to enter a length in feet. The program should then give the user the option to convert from feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they enter a 2, then the program converts to yards, etc. While this can be done with if statements, it is much shorter with lists and it is also easier to add new conversions if you use lists.
"""
print('*'*80)

feet = eval(input('Enter length in feet: '))
#inches, yards, miles, millimeters, centimeters, meters, kilometers
lengths = [feet * 12, feet * 0.3334, feet * 1.8939e-4, feet * 304.8, feet * 30.48, feet * 0.3048, feet * 0.0003048]

choice = eval(input('Choose to convert:\n0. inches\n1. yards\n2. miles\n3. millimeters\n4. centimeters\n5. meters\n6. kilometers\n\t:'))

print('Converted length:', lengths[choice])

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter length in feet: 35.43
Choose to convert:
0. inches
1. yards
2. miles
3. millimeters
4. centimeters
5. meters
6. kilometers
        :2
Converted length: 0.0067100877
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter length in feet: 35.43
Choose to convert:
0. inches
1. yards
2. miles
3. millimeters
4. centimeters
5. meters
6. kilometers
        :0
Converted length: 425.15999999999997
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter length in feet: 35.43
Choose to convert:
0. inches
1. yards
2. miles
3. millimeters
4. centimeters
5. meters
6. kilometers
        :1
Converted length: 11.812361999999998
********************************************************************************
"""