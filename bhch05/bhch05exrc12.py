"""
@@@@ Program statement:
Write a program that asks the user to guess a random number between 
1 and 10. If they guess right, they get 10 points added to their 
score, and they lose 1 point for an incorrect guess. Give the user 
five numbers to guess and print their score after all the guessing is done.
"""
from random import randint
score=0
for i in range(5):
    guess = eval(input('Guess a number between 1 and 10: '))
    value = randint(1,10)
    print('Randomly generated number: ', value)
    if guess == value:
        score = score + 10;
    else:
        score = score - 1

print('You scored', score, 'points')