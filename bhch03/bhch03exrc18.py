print('A dollar is worth 100 cents.')
print('A penny is worth 1 cent.')
print('A nickel is worth 5 cents.')
print('A dime is worth 10 cents.')
print('A quarter is worth 25 cents.')
print('')

amt = eval(input('Enter an amount of change less than $1.00: '))

pieces = amt*100

quarter = pieces // 25
pieces = pieces - quarter * 25

dime = pieces // 10
pieces = pieces - dime * 10

nickel = pieces // 5
pieces = pieces - nickel * 5

cents = pieces

print(quarter, 'quarters,', dime, 'dimes,', nickel, 'nickel and', cents, 'cents are needed to efficiently make the entered change.')