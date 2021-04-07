"""
@@@@ Program statement:
Write a program that asks the user to enter a number and prints the 
sum of the divisors of that number. The sum of the divisors of a 
number is an important function in number theory.
"""
number = eval(input('Enter a number: '))
sum = 0
for i in range(number, 0, -1):
    if(number % i == 0):
        sum = sum + i
        print(i)
print('SUM of the divisors of the given number =', sum)