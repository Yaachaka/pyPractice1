"""
bhch09exrc15.py: Write a program to play the following game. There is a list of several country names and the program randomly picks one. The player then has to guess letters in the word one at a time. Before each guess the country name is displayed with correctly guessed letters filled in and the rest of the letters represented with dashes. For instance, if the country is Canada and the player has correctly guessed a, d, and n, the program would display -ana-da. The program should continue until the player either guesses all of the letters of the word or gets five letters wrong.
"""
print('*'*80)

from random import randint

countries = ['india', 'america', 'england', 'china', 'russia', 'japan', 'australia', 'pakistan', 'argentina', 'canada', 'madagascar', 'tanzania', 'mauritania', 'malaysia', 'morocco']

#countries = ['australia', 'madagascar', 'tanzania', 'mauritania', 'malaysia', 'morocco']

choice = countries[randint(0, len(countries)-1)]
wrong_guess = 5

guessed = ['-']*len(choice)
while wrong_guess:
    guess = input('Guess a letter: ')
    guess = guess[0]
    if guess in choice:
        c1 = choice.count(guess)
        c2 = guessed.count(guess)
        if c1 > c2:
            ind = choice.index(guess)
            pos = ind
            for i in range(c2):
                ind = choice[pos+1:].index(guess)
                pos = pos + ind + 1
            guessed[pos] = guess
            if ''.join(guessed) == choice:
                    print('You got it right.')
                    break
            print(str(guessed))
        else:
            wrong_guess = wrong_guess - 1
            print('Wrong guess :(')
    else:
        wrong_guess = wrong_guess - 1
        print('Wrong guess :(')

if not wrong_guess:
    print('\nYou failed to guess the country name.')
print('It was', choice)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
*******************************************************************************
Guess a letter: g
Wrong guess :(
Guess a letter: a
['-', 'a', '-', '-', '-', '-', '-', '-']
Guess a letter: m
Wrong guess :(
Guess a letter: t
['t', 'a', '-', '-', '-', '-', '-', '-']
Guess a letter: a
['t', 'a', '-', '-', 'a', '-', '-', '-']
Guess a letter: a
['t', 'a', '-', '-', 'a', '-', '-', 'a']
Guess a letter: n
['t', 'a', 'n', '-', 'a', '-', '-', 'a']
Guess a letter: z
['t', 'a', 'n', 'z', 'a', '-', '-', 'a']
Guess a letter: n
['t', 'a', 'n', 'z', 'a', 'n', '-', 'a']
Guess a letter: i
You got it right.
It was tanzania
********************************************************************************

@@@@ Trial2:
********************************************************************************
Guess a letter: c
Wrong guess :(
Guess a letter: h
Wrong guess :(
Guess a letter: a
['-', '-', '-', '-', 'a']
Guess a letter: i
['i', '-', '-', '-', 'a']
Guess a letter: n
['i', 'n', '-', '-', 'a']
Guess a letter: d
['i', 'n', 'd', '-', 'a']
Guess a letter: i
You got it right.
It was india
********************************************************************************

@@@@ Trial3:
********************************************************************************
Guess a letter: a
['-', '-', '-', '-', 'a']
Guess a letter: c
Wrong guess :(
Guess a letter: h
Wrong guess :(
Guess a letter: k
Wrong guess :(
Guess a letter: n
['-', 'n', '-', '-', 'a']
Guess a letter: d
['-', 'n', 'd', '-', 'a']
Guess a letter: u
Wrong guess :(
Guess a letter: s
Wrong guess :(

You failed to guess the country name.
It was india
********************************************************************************
"""
