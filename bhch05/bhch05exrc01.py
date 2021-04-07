"""
@@@@ Program Statement: 
Write a program that counts how many of the squares of the numbers from 1 
to 100 end in a 1.
"""
count=0
for i in range(1,101):
    if((i**2)%10==1):
        count=count+1;
        print(i**2)
print('There are ',count,' numbers whose last digit is 1 on squaring (between 1 and 100)')