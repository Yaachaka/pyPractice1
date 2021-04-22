"""
@@@@ Program statement:
An integer is called squarefree if it is not divisible by any perfect 
squares other than 1. For instance, 42 is squarefree because its 
divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those numbers 
(except 1) is a perfect square. On the other hand, 45 is not 
squarefree because it is divisible by 9, which is a perfect square. 
Write a program that asks the user for an integer and tells them if 
it is squarefree or not.
"""

print('Program to check if an integer is SQUAREFREE')
print('An integer is called squarefree if it is not divisible by any perfect squares other than 1.')

from math import sqrt, floor
number = eval(input('Enter a number: '))

flag = 0
for i in range(number, 1, -1):
	if number % i == 0:
		if sqrt(i) == floor(sqrt(i)):
			flag = 1
		
if flag == 0:
    print('The given number is squarefree.')
else:
    print('The given number is not sqarefree.')