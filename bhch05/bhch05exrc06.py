"""
@@@@ Program Statement: 
A number is called a perfect number if it is equal to the sum of all of 
its divisors, not including the number itself. For instance, 6 is a 
perfect number because the divisors of 6 are 1, 2, 3, 6 and 6 = 1 + 2 + 3. 
As another example, 28 is a perfect number because its divisors are 
1, 2, 4, 7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not 
a perfect number because its divisors are 1, 3, 5, 15 and 
15 != 1 + 3 + 5. Write a program that finds all four of the 
perfect numbers that are less than 10000.
"""
print('Perfect numbers between 1 and 10000')
print(1, end = ' ')
for j in range(1,10001):
    sum = 0
    for i in range(j-1, 0, -1):
        if(j % i == 0):
            sum = sum + i
    if(sum == j):
        print(j, end=' ')