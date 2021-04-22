print('A jar of Halloween candy contains unknown number of candy.')
print('If you can guess exactly how much candy is in the bowl...')
print('then you win all the candy.')
print()
print('Hint on observing the jar: The jar contains less than 200 pieces of candy.')
print('Hints from the shopkeeper: ')
print(' Hint1: If the candies are evenly divided among 5 people then 2 candies are left.')
print(' Hint2: If the candies are evenly divided among 6 people then 3 candies are left.')
print(' Hint3: If the candies are evenly divided among 7 people then 2 candies are left.')

guess=eval(input('Guess the number of candies in the jar: '))
for i in range(12,200):
    if i % 5 == 2:
        if i % 6 == 3:
            if i % 7 == 2:
                print('Number of candies in jar: ', i)
                if guess == i:
                    print('WOWWWWW... This jar of candies is yours.')