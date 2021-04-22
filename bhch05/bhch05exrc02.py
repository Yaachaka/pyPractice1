"""
@@@@ Program Statement:
Write a program that counts how many of the squares of the numbers from 1 to 
100 end in a 4 and how many end in a 9.
"""

count1=0
count2=0

for i in range(1, 101):
    if((i**2) % 10 == 4):
        count1 = count1 + 1
        print(i**2)
    if((i**2) % 10 == 9):
        count2 = count2 + 1;
        print(i**2)
print('There are ', count1, ' numbers whose last digit is 4 on squaring (between 1 and 100)')
print('There are ', count2, ' numbers whose last digit is 9 on squaring (between 1 and 100)')