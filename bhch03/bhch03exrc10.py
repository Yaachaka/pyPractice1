power = eval(input('Enter a power: '))
print('Last digit of the value 2 raised to', power, 'is', (2**power)%10)

power = eval(input('Enter a power: '))
print('Last two digits of the value 2 raised to', power, 'is', (2**power)%100)

power = eval(input('Enter a power: '))
lastDigits = eval(input('How many last digits to print?: '))
print('Last', 10**lastDigits, 'digits of the vaslue raised to', power, 'is', (2**power)%(10**lastDigits))
