"""
@@@@ Program statement:
Write a program that asks the user to enter a value n, and then 
computes (1 + 1/2 + 1/3 + ... + 1/n) - ln(n). The ln function is 
log in the math module.
"""
number=eval(input('Enter a number: '))
sum=0
from math import log    #natural log

for i in range(1, number+1):
    sum=sum+round(1/i,4)
print('sum =', sum)
total = sum - log(number)
total = round(total, 4)
print('Total=', total)