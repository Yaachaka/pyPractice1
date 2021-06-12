"""
bhch09exrc09.py: A 4000-year old method to compute the square root of 5 is as follows: Start with an initial guess, say 1. Then compute (1 + (5/1))/(2) = 3. Next, take that 3 and replace the 1’s in the previous formula with 3’s . This gives (3 + 5/3)/2 = 7/3 ≈ 2.33. Next replace the 3 in the previous formula with 7/3. This gives ((7/3) + 5/(7/3))/2 = 47/21 ≈ 2.24. If you keep doing this process of computing the formula, getting a result, and plugging it back in, the values will eventually get closer and closer to √5. This method works for numbers other than 5. Write a program that asks the user for a number and uses this method to estimate the square root of the number correct to within 10^-10. The estimate will be correct to within 10^-10 when the absolute value of the difference between consecutive values is less than 10^-10.
"""
print('*'*80)

from math import sqrt
number = eval(input('Enter a number to find square root: '))
print('Result using inbuilt modules:', sqrt(number))
print('Result from our calculation(old method): ', end='')

diff = 1

temp1 = (1 + (number/1))/2

while diff > 10e-10:
	temp2 = (temp1 + (number/temp1))/2
	diff = temp1 - temp2
	temp1 = temp2

print(temp1)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a number to find square root: 4
Result using inbuilt modules: 2.0
Result from our calculation(old method): 2.0
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a number to find square root: 76
Result using inbuilt modules: 8.717797887081348
Result from our calculation(old method): 8.717797887081346
********************************************************************************
"""